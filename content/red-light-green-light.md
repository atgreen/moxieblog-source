Title: Evaluating DejaGnu results with Red Light Green Light
Date: 2019-12-14
Author: green
Category: moxie
Tags: rlgl
Slug: red-light-green-light

Last year I hacked up a tool in frustration called [Red Light Green
Light](https://rl.gl) (rlgl) -- a proof-of-concept effort to
demonstrate a git-centric way to manage "quality gates" in a CI/CD
pipeline.

A CI/CD quality gate is a process that evaluates the quality of a
software artefact before allowing it to proceed to the next stage of
the pipeline.  For example, you may have a quality gate that examines
the results of a container security scan report before pushing your
container image into a registry.

It's probably worth reading the [Red Light Green Light
README](https://github.com/atgreen/red-light-green-light/blob/master/README.md)
before continuing here, but the basic idea is that we normalize test
evaluation reports into JSON format, and them match those against JSON
matching objects stored in a git repo to come up with either a Red
Light or a Green Light.  The resulting rlgl HTML report identifies how
the PASS/FAIL/XFAIL patterns were matched along with links to the git
commits for the matching policy.  Here's a picture..

<center>
![](http://moxielogic.github.io/images/rlgl-workflow.png)
</center>

The benefits of this approach in a large regulated environment with
segregated roles and duties are many:

* Evaluation policy is no longer locked within proprietary tools
* There's a well defined workflow for policy change management (pull requests)
* Authentication and authorization for policy management is a solved problem
* The policy change history is easily auditable

But as I was preparing a new release of
[libffi](https://github.com/libffi/libffi), another FOSS package I
maintain, I realized that Red Light Green Light could easily be
adapted to examine [DejaGnu](https://www.gnu.org/software/dejagnu/)
test results.  This turned out to be a great idea.

We use [travis-ci](https://travis-ci.org/libffi/libffi) to test
changes to libffi.  This is critical because libffi is a complex and
fragile peice of software -- a mix of C and assembly code that has
been ported to almost 30 major processor architectures.  Automated CI
testing is important because I can't expect every contributor to test
their changes on those 30 targets (combined with different compiler
and OS ABIs, the test matrix explodes quickly).

I was recently looking at the moxie-elf GCC testresults (posted
nightly to the [gcc-testresults mailing
list](https://gcc.gnu.org/ml/gcc-testresults/)) and realized that,
once again, Red Light Green Light could help me get a handle on the
test failures.  I was looking to solve three problems:

* I needed a place to maintain state on test failures -- notes for
  myself that I can refer to when I have time to continue
  investigating.  I work on moxie sporadically, often with many month
  gaps, so having the ability to annotate test failures with notes is
  important.

* I needed a way to track regressions, so I can easily see when tests
  that were once passing start failing.  This would be easy if every
  test was known to pass, but I am far from that.

* I needed a way to track new failures for new test cases added by the
  GCC developers.  Again, this would be easy if every test was known
  to pass, but not so easy if you have a collection of failures
  already.

Once again, this turned out to be a great idea.  I've tracked down
almost every test failure and recorded them in a policy repo at
[https://github.com/moxielogic/rlgl-toolchain-policy](https://github.com/moxielogic/rlgl-toolchain-policy).
I'm able to watch for regressions, new test failures and keep notes
related to my debugging efforts.  All of the good bits are in the
policy's [XFAIL
file](https://github.com/moxielogic/rlgl-toolchain-policy/blob/master/XFAIL).

I run the test result evaluation after my nightly 'make check' run like so:

```bash
wget -qO - https://rl.gl/cli/rlgl-linux-amd64.tgz | \
    tar --strip-components=2 -xvzf - ./rlgl/rlgl
./rlgl login https://rl.gl
export RLGL=$(./rlgl e --id=$(./rlgl start) --policy https://github.com/moxielogic/rlgl-toolchain-policy.git $(find . -name gcc.sum) || true)
```

At this point the `RLGL` environment variable contains the result of
the evaluation.  Something like `RED:
https://rl.gl/doc?id=RLGL-2FWVG23I`, which I just paste into the
results that get posted to the mailing list.

Here's what a sample report looks like:
<center>
![](http://moxielogic.github.io/images/rlgl-dg.png)
</center>

Feel free to try [Red Light Green Light](https://rl.gl) out.  You can
host it yourself, or use my experimental hosted version at
[https://rl.gl](https://rl.gl).  All documents are reports are
currently set to expire after 7 days.

As always, feedback welcome!
