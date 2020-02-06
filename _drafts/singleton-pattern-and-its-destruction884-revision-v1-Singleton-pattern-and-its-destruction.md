---
id: 2109
title: Singleton pattern and its destruction
date: 2019-10-08T18:22:14+05:30
author: Pradeep Pant
layout: revision
guid: http://pradeeppant.com/2019/10/884-revision-v1/
permalink: /2019/10/08/884-revision-v1/
---
The Singleton pattern is remarkably simple.  Its intent states, Ensure a class only has one instance, and provide a global point of access to it. It&#8217;s also flexible.  It helped us encapsulate the creation of User objects, which give file system users the authority to access their own files and no one else&#8217;s.  To obtain a User object, a client program calls a static User::LogIn operation:

static const User\* User::LogIn(const char\* loginName, const char* password);

This of course is just a gussied-up version of Singleton&#8217;s static Instance operation.  In the vanilla version of the pattern, Instance limits you to exactly one instance of the Singleton class (the User class in this case).  But one of the pattern&#8217;s consequences is the option to control the number of instances, as opposed to flatly precluding more than one.  We availed ourselves of that option to preclude more than one User instance per user.  That way an application is free to create multiple instances if it caters to multiple users at once.  Another thing which is impotant that the pattern&#8217;s deafening silence on the issue of deletion.  Who deletes Singleton instances, and how, and when?  The words &#8220;delete&#8221; and &#8220;destructor&#8221; never appear in the pattern.  Honest oversight?  Conscious omission?  Or perhaps evading a hard problem?  This article will try to convince you that it&#8217;s neither of the last two.  We&#8217;ll also look at an assortment of new observations on this surprisingly rich little pattern.

I.  THE ALL-IMPORTANT DESTRUCTOR  Like any self-respecting class, a Singleton class should define a destructor.  If Singleton is to be subclassed, then the destructor should be declared virtual.  All just C++ 101.  Now comes the tricky part: Should this destructor be public, private, or protected?  &#8220;What&#8217;s the issue?&#8221; you might ask.  &#8220;Make it public and be done with it.&#8221;  The implication here is that singleton destruction is \*explicit\*&#8212;that is, it&#8217;s a client responsibility.     But there&#8217;s a reasonable argument against that. The Singleton pattern places responsibility for object \*creation\* squarely in the Singleton class.  Clients go to this class to get a singleton instance.  So if a client \*deletes\* the instance without the Singleton class knowing about it, from then on the Singleton class will hand out &#8220;dangling references,&#8221; which point to objects that no longer exist.  Singleton&#8217;s responsibilities imply that it \*owns\* the instance it creates; and ownership, finally, means responsibility for deletion.  This is in contrast to other creational patterns, such as Abstract Factory and Factory Method, that do not retain ownership of the instances they create.  That said, we might still get away with a public destructor \*if\* the following are true:    * The destructor deletes and cleans up its references to the static     instance.  Then a subsequent call to the Instance operation will  work as it did the first time. Clients do not retain references to the Singleton object. Otherwise, they would be left with dangling references.  These restrictions are stringent enough to make explicit destruction the exception rather than the rule.  In our file system design, for example, we have to consider how and when User objects get deleted. Suppose we let clients delete User objects explicitly with the normal delete operator.  We could be even more explicit and provide a static LogOut operation that mirrors the LogIn operation (either way; the deletion interface doesn&#8217;t really matter).  Currently there&#8217;s no way for the User class&#8212;a kind of Singleton&#8212;to know which clients have references to User objects.  So if a User gets deleted, clients will end up with dangling references.  Thoroughly unacceptable.  While we probably need a mechanism for logging users out, say, for bookkeeping purposes, the potential for dangling references tells us that we can&#8217;t use deletion as the log-out mechanism.  In other words, we shouldn&#8217;t confuse logging out with deleting a User object. Whatever interface we choose for logging a user out, it cannot involve explicit destruction of a User object.  The point of all this is to make the case for rejecting the public destructor.  Rejecting a private destructor is much easier: we want to allow subclassing the Singleton class, after all.  That leaves only one choice&#8212;a protected destructor.  Back now to square one: How does a Singleton ever get deleted?

II.  IMPLICIT DESTRUCTION  The thing about Singleton objects is that they are usually, if not inherently, long-lived.  Often they exist for the life of the program. You delete them not so much to reclaim space but to shut down in an orderly manner.  You want to close files, unlock resources, terminate network connections, and so forth, without the appearance of an abrupt termination (read &#8220;crash&#8221;).  If your Singleton objects ever need to do such cleanup, they probably have to wait until just before the program terminates.  This is a nice property, because it means C++ may be able to do the deletion for us implicitly.  C++ deletes static objects automatically at program termination.  The language guarantees that their destructors will be called and space reclaimed at that time, although it doesn&#8217;t guarantee the calling order.  For now let&#8217;s assume that ordering isn&#8217;t a problem; there is only one singleton in the program, or if there is more than one, their destruction is not order-dependent.  Now we can define the Singleton class like this:

<pre>class Singleton {    

public:        

static Singleton* Instance();    

protected:        

Singleton() { }         

 friend class SingletonDestroyer;        

virtual ~Singleton() { }    

private:        

 static Singleton* _instance;        

 static SingletonDestroyer _destroyer;     };     

Singleton* Singleton::_instance = 0;    

SingletonDestroyer Singleton::_destroyer;     

Singleton* Singleton::Instance () {        

if (!_instance) {             _instance = new Singleton;            

_destroyer.SetSingleton(_instance);         }        

return _instance;     } 

where SingletonDestroyer is a class whose sole purpose is the destruction of a particular Singleton object:     

class SingletonDestroyer {    

public:        

SingletonDestroyer(Singleton* = 0);        

~SingletonDestroyer();         

void SetSingleton(Singleton* s);    

private:        

Singleton* _singleton;     };     

SingletonDestroyer::SingletonDestroyer (Singleton* s) {        

 _singleton = s;     }     

SingletonDestroyer::~SingletonDestroyer () {        

delete _singleton;     }     

void SingletonDestroyer::SetSingleton (Singleton* s) {        

_singleton = s;     }</pre>

The Singleton class declares a static SingletonDestroyer member, which gets created automatically at program startup.  If and when the user first calls Singleton::Instance, not only will the Singleton object get created, but Instance will also pass that object to the static SingletonDestroyer object, effectively transferring ownership to the SingletonDestroyer.  When the program exits, the SingletonDestroyer will be destroyed, and the Singleton object with it.  Singleton destruction is now implicit.  Simple&#8212;almost.  Note the \*friend\* declaration in the declaration of the Singleton class.  It&#8217;s needed to give the destroyer access to Singleton&#8217;s protected destructor.  Not pretty if you have an aversion to the \*friend\* keyword, but it&#8217;s necessary, given the earlier arguments against a public destructor.  And it exemplifies what is perhaps the most defensible use of \*friend\*: to define another level of protection, as opposed to providing a work-around for a bad design.  To maximize reuse, especially if there are multiple kinds of singletons in your program, you might save yourself some typing and define a templatized Destroyer class

template <class DOOMED>     class Destroyer {

public:         Destroyer(DOOMED* = 0);

~Destroyer();

void SetDoomed(DOOMED*);

private:         // Prevent users from making copies of a          // Destroyer to avoid double deletion:         Destroyer(const Destroyer<DOOMED>&);

void operator=(const Destroyer<DOOMED>&);

private:         DOOMED* _doomed;     };

template <class DOOMED>

Destroyer<DOOMED>::Destroyer (DOOMED* d) {

_doomed = d;     }

template <class DOOMED>     Destroyer<DOOMED>::~Destroyer () {

delete _doomed;     }

template <class DOOMED>     void Destroyer<DOOMED>::SetDoomed (DOOMED* d) {

_doomed = d;     }

That lets us define Singleton like this:

class Singleton {

public:         static Singleton* Instance();

protected:

Singleton() { }

friend class Destroyer<Singleton>;

virtual ~Singleton() { }

private:

static Singleton* _instance;

static Destroyer<Singleton> _destroyer;     };

Singleton* Singleton::_instance = 0;

Destroyer<Singleton> Singleton::_destroyer;

Singleton* Singleton::Instance () {

if (!\_instance) {             \_instance = new Singleton;

\_destroyer.SetDoomed(\_instance);         }

return _instance;     }

III. NOTHING&#8217;S PERFECT  There are two potential problems with implicit destruction.  First, it doesn&#8217;t help you if you need to delete your singleton \*before\* the end of the program.  In that case, it&#8217;s hard to imagine an approach that doesn&#8217;t require explicit destruction.  Moreover, you&#8217;ll either have to add mechanism (say, reference-counting) to minimize the dangling reference problem, or you&#8217;ll have to force clients to access the Singleton instance exclusively through the Singleton::Instance operation.  One way to do the latter involves

(1) making Instance return a reference to a Singleton and

(2) disallowing copy and initialization by declaring the assignment and copy constructors

private:

class Singleton {

public:

static Singleton& Instance();

protected:         // &#8230;

private:         Singleton(const Singleton&);

Singleton& operator=(const Singleton&);         // &#8230;     };

This approach isn&#8217;t foolproof, unfortunately, since a client can always take the address of the value that Instance returns, or it can cast away these safeguards entirely.  Nevertheless, this issue is unlikely to be a show-stopper.  As pointed out earlier, the Singleton pattern favors long-lived objects.  So explicit deletion probably won&#8217;t be a common problem.  The second problem surfaces when you&#8217;ve got multiple singleton objects in your program, and they depend on each other.  In that case, the order of destruction might be significant.  Consider our file system design, where we&#8217;ve applied the Singleton pattern twice.  We used it first to control the number of User objects, which produced the singleton User class.  The second application ensured just one Grouping object, which defines a mapping between users and the groups they belong to.  The Grouping object lets us define protection for groups of users rather than just individuals. Because it doesn&#8217;t make sense (it&#8217;s downright dangerous, in fact) to have more than one grouping active at once, we made the Grouping class a Singleton.  A Grouping object maintains references both to User objects and to Group objects.  It doesn&#8217;t own the User objects, but it could conceivably own the Group objects.  Either way, it seems desirable to delete the Grouping object before the User objects, just on principle. True, the dangling references that would otherwise result probably won&#8217;t be a problem, since Grouping shouldn&#8217;t have to dereference any of them during its destruction&#8212;but then again, you never know.  My point is this: the destroyer approach, based as it is on an unspecified language implementation mechanism, begins to fray when destruction order is important.  If your application calls for multiple, dependent singletons, then you may have to revert to explicit destruction.  One thing&#8217;s for sure: you can&#8217;t use more than one destroyer if the singleton destructors depend on one another.  An alternative is to eschew destroyers altogether and rely instead on the draft-standard atexit() function, it is a good way to cleanup singletons in C++ when you really want single instances with program lifetime and no replacement.  The draft standard promises a lot:

The function atexit() from <cstdlib> can be used to specify a function to be called at exit.  If atexit() is         to be called, the implementation shall not destroy objects initialized before an atexit() call until after the     function specified in the atexit() call has been called. The only way in which it fails is if a statically     initialized object whose destructor depends on a Singleton instance is initialized \*after\* the Singleton instance is  constructed, i.e., through some other static initialization.  This suggests that classes having static instances should avoid depending on singletons during destruction.  (Or at least there should be a way for such classes to check for the existence of the Singleton during destruction.)  While this obviates the need for destroyers, the real problem&#8212;deleting mutually-dependent singletons&#8212;remains.  Garbage collection, anyone?

IV. ODDS AND SODS  Long ago, in a galaxy far, far away, Scott Meyers posited the following: My [version of Singleton] is quite similar to yours, but instead of using a class static and having Instance return a pointer, I use a function static and return a reference:

Singleton& Singleton::Instance () {

static Singleton s;

return s;         }

This seems to offer every advantage your solution does (no construction if never used, no dependence on initialization order between translation units, etc.), plus it allows users to use object syntax instead of pointer syntax.  Furthermore, the above solution makes it much less likely a caller will inadvertently delete the singleton in a misguided attempt to avoid a memory leak.  The article overlooking a reason for returning a pointer to a class  static instead of a reference to a function static?  The only drawback here is that it makes it hard to extend the Singleton through subclassing, since Instance will always create an object of type Singleton.  Besides, one needn&#8217;t worry about deleting the Singleton instance if its destructor isn&#8217;t public.  While by having a slight preference for returning a reference, in the end it seems to make little difference.  Later, Erich Gamma noticed a more fundamental problem with this approach: It turns out that it is not possible to make [Scott&#8217;s approach]  thread-safe if multiple threads can call Instance. The problem is  that [some C++ compilers generate] some internal data structures that cannot be protected by locks. In such situations you would have to acquire the lock at the call site&#8212;pretty ugly.  Yep.  And it wouldn&#8217;t be long before Doug Schmidt got bitten by this very bug:

References:

C++ Report &#8220;Pattern Hatching&#8221; column for June &#8217;96 issue John Vlissides;  http://www.cs.wustl.edu/~schmidt/TSS-pattern.ps.gz  Schmidt, D. Electronic mail communication, February 8, 1996.  Column Without a Name, February &#8217;95.  Gamma, E., R. Helm, R. Johnson, J. Vlissides.  \*Design Patterns: Elements of Reusable Object-Oriented Software,\* Addison-Wesley, Reading, MA, 1995