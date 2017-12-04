Cromlech ZODB Demo
========================

There is also another richer
[Demo](https://github.com/Cromlech/CromlechCromDemo)
without the ZODB.

Installation instructions are in [INSTALL.md](./INSTALL.md)

Cromlech is a rewrite  of Grok, written by one of 
the original Grok contributors, Souheil Chelfouh.  It is in daily
production use in a big company in Germany, and in
daily development use by its author Souheil.

Why use Cromlech instead of Grok? There seeral reasons.  Cromlech is already
ported to Python 3.  It uses Zeam instead of zope.formli and z3c.form.  It has
a much cleaner implementation of security on views.  No more security proxies
on objects.  Let us dig deeper into these issues. 

For me the biggest reason is that cromlech
is already running in Python 3, while Grok has some
15-24 packages which need to be ported.  

The other reason is that we are now much smarter than when grok was written.
zope.formlib and z3c.form had way way too many adapters.  Zeam.form is much
better designed.   Grok is really tied in with the a single root ZODB, Cromlech
can optionally use one or more ZODBs. Cromlech can also do traversal or
dispatch.  In my case I intend to do the simple thing, and just have a
single ZODB app using traversal.

How does Cromlech differ from Grok?   Both are based on the ZTK.
The big difference is that Cromlech uses the more modern WebOb,
while grok/zope are still using the older zope.pulisher.
(Did I get that right?????).

The next big difference is  in the security model.  The
modern way to do security is security on views.
ZTK also does security on object access.
So Grok has to patch that leading to a lot of additional complexity.
Cromlech takes the simpler approach of directly downg security on views.

Cromlech uses Zeam.form, while Grok uses
zope.formlib and Z3c.form.  The problem with the later two is that they
have a lot of extra adaptors, leading to unnecessary complexity.  Even
Jim Fulton said something like: “We used way too many adaptors.”  And of
course zeam.form can also be used with Grok or Plone.


Cromlech has a new component registry.
While it is plug compatible with the old registry, it allows for chaining of
registries.  Think a tree of registries.

Cromlech startup is a bit different than Grok.  Grok just had one way to
start up.  Cromlech has an app.py file which configures your startup.
It gives you a much more flexible  approach than the grok approach. 


So why not just use Pyramid?  The reason that I like Grok or Cromlech is
that they are rich environments.  They give you a lot of concepts to build
on.  In contrast Pyramid is quite stripped down.  Optimized for computer speed,
rather than ease of development.  In particular zope.securitypolish has not
een ported to Pyramid.  Maybe it cannot be. 


Pyramid is another bulky framework, whereas Cromlech is more a collection of
separate tools.

Martian Vs Venusian.
Grok does configuration using martian.  Cromlech
uses Venutian.  What is the difference?

Martian  uses declarations.   Here is an example.

```
class AuditAccount(grok.View):
   grok.context(IAccount)
   grok.name ("audit")
   grok.require("banking.auditAccount")
```

Venutian uses decorators  Here is an example from the Pyramid documentation.
Although I believe the cromlech decorators are a bit different.


```
@view_config()
def my_view(request):
    """ My view “""
    return Response()
```

The senior developers prefer decorators.  Simpler to implement and do not 
inherit.  The junior developers prefer martian.  Easier to understand.  
Does inheritance properly.  In many cases you do not have to do anything, 
inheritance does it for you.  It looks just like regular code.  But of 
course open source is written by the senior developers, for the senior 
developers, so Martian has sadly mostly passed out of use.  
For those who do prefer Martian, the good news is that it is already running on
Python 3.  But there are many special grokkers in Grok, and reportedly as of 
middle 2017, not all of them work  with Martian on Python 3. 


As for Grok?  Cromlech is built on top of the ZTK, so mostly they should be 
compatible.  Once I figure out the Cromlech libraries, it should not be that 
hard to port a Grok application over.  My hope is that porting a Grok 
application to Cromlech will only require upgrading a few grok packages to 
Python 3.  Time will tell. 

There are additional docs [here](./src/cromdemo/docs).