%define name python27-boto
%define pythonname boto
%define version 2.38.0
%define unmangled_version 2.38.0
%define release 1

%define __os_install_post\
%( rpm --eval %%__os_install_post)\
( cd $RPM_BUILD_ROOT; find . -type f | sed -e 's/^.//') > INSTALLED_FILES
Summary: Amazon Web Services Library
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{pythonname}-%{unmangled_version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{pythonname}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Mitch Garnaat <mitch@garnaat.com>
Url: https://github.com/boto/boto/

%description
####
boto
####
boto 2.38.0

Released: 9-Apr-2015

.. image:: https://travis-ci.org/boto/boto.svg?branch=develop
        :target: https://travis-ci.org/boto/boto

.. image:: https://pypip.in/d/boto/badge.svg
        :target: https://pypi.python.org/pypi/boto/

************
Introduction
************

Boto is a Python package that provides interfaces to Amazon Web Services.
Currently, all features work with Python 2.6 and 2.7. Work is under way to
support Python 3.3+ in the same codebase. Modules are being ported one at
a time with the help of the open source community, so please check below
for compatibility with Python 3.3+.

To port a module to Python 3.3+, please view our `Contributing Guidelines`_
and the `Porting Guide`_. If you would like, you can open an issue to let
others know about your work in progress. Tests **must** pass on Python
2.6, 2.7, 3.3, and 3.4 for pull requests to be accepted.

******
Boto 3
******
The next major version of Boto is currently in developer preview and can
be found in the `Boto 3 <https://github.com/boto/boto3#readme>`__
repository and installed via ``pip``. It supports the latest service APIs
and provides a high-level object-oriented interface to many services.

Please try Boto 3 and
`leave feedback <https://github.com/boto/boto3/issues>`__ with any issues,
suggestions, and feature requests you might have.

********
Services
********

At the moment, boto supports:

* Compute

  * Amazon Elastic Compute Cloud (EC2) (Python 3)
  * Amazon Elastic Map Reduce (EMR) (Python 3)
  * AutoScaling (Python 3)
  * Amazon Kinesis (Python 3)
  * AWS Lambda (Python 3)
  * Amazon EC2 Container Service (Python 3)

* Content Delivery

  * Amazon CloudFront (Python 3)

* Database

  * Amazon Relational Data Service (RDS)
  * Amazon DynamoDB (Python 3)
  * Amazon SimpleDB (Python 3)
  * Amazon ElastiCache (Python 3)
  * Amazon Redshift (Python 3)

* Deployment and Management

  * AWS Elastic Beanstalk (Python 3)
  * AWS CloudFormation (Python 3)
  * AWS Data Pipeline (Python 3)
  * AWS Opsworks (Python 3)
  * AWS CloudTrail (Python 3)
  * AWS CodeDeploy (Python 3)

* Administration & Security

  * AWS Identity and Access Management (IAM) (Python 3)
  * AWS Key Management Service (KMS) (Python 3)
  * AWS Config (Python 3)
  * AWS CloudHSM (Python 3)

* Application Services

  * Amazon CloudSearch (Python 3)
  * Amazon CloudSearch Domain (Python 3)
  * Amazon Elastic Transcoder (Python 3)
  * Amazon Simple Workflow Service (SWF) (Python 3)
  * Amazon Simple Queue Service (SQS) (Python 3)
  * Amazon Simple Notification Server (SNS) (Python 3)
  * Amazon Simple Email Service (SES) (Python 3)
  * Amazon Cognito Identity (Python 3)
  * Amazon Cognito Sync (Python 3)
  * Amazon Machine Learning (Python 3)

* Monitoring

  * Amazon CloudWatch (EC2 Only) (Python 3)
  * Amazon CloudWatch Logs (Python 3)

* Networking

  * Amazon Route53 (Python 3)
  * Amazon Route 53 Domains (Python 3)
  * Amazon Virtual Private Cloud (VPC) (Python 3)
  * Elastic Load Balancing (ELB) (Python 3)
  * AWS Direct Connect (Python 3)

* Payments and Billing

  * Amazon Flexible Payment Service (FPS)

* Storage

  * Amazon Simple Storage Service (S3) (Python 3)
  * Amazon Glacier (Python 3)
  * Amazon Elastic Block Store (EBS)
  * Google Cloud Storage

* Workforce

  * Amazon Mechanical Turk

* Other

  * Marketplace Web Services (Python 3)
  * AWS Support (Python 3)

The goal of boto is to support the full breadth and depth of Amazon
Web Services.  In addition, boto provides support for other public
services such as Google Storage in addition to private cloud systems
like Eucalyptus, OpenStack and Open Nebula.

Boto is developed mainly using Python 2.6.6 and Python 2.7.3 on Mac OSX
and Ubuntu Maverick.  It is known to work on other Linux distributions
and on Windows.  Most of Boto requires no additional libraries or packages
other than those that are distributed with Python.  Efforts are made
to keep boto compatible with Python 2.5.x but no guarantees are made.

************
Installation
************

Install via `pip`_:

::

    $ pip install boto

Install from source:

::

    $ git clone git://github.com/boto/boto.git
    $ cd boto
    $ python setup.py install

**********
ChangeLogs
**********

To see what has changed over time in boto, you can check out the
release notes at `http://docs.pythonboto.org/en/latest/#release-notes`

***************************
Finding Out More About Boto
***************************

The main source code repository for boto can be found on `github.com`_.
The boto project uses the `gitflow`_ model for branching.

`Online documentation`_ is also available. The online documentation includes
full API documentation as well as Getting Started Guides for many of the boto
modules.

Boto releases can be found on the `Python Cheese Shop`_.

Join our IRC channel `#boto` on FreeNode.
Webchat IRC channel: http://webchat.freenode.net/?channels=boto

Join the `boto-users Google Group`_.

*************************
Getting Started with Boto
*************************

Your credentials can be passed into the methods that create
connections.  Alternatively, boto will check for the existence of the
following environment variables to ascertain your credentials:

**AWS_ACCESS_KEY_ID** - Your AWS Access Key ID

**AWS_SECRET_ACCESS_KEY** - Your AWS Secret Access Key

Credentials and other boto-related settings can also be stored in a
boto config file.  See `this`_ for details.

.. _Contributing Guidelines: https://github.com/boto/boto/blob/develop/CONTRIBUTING
.. _Porting Guide: http://boto.readthedocs.org/en/latest/porting_guide.html
.. _pip: http://www.pip-installer.org/
.. _release notes: https://github.com/boto/boto/wiki
.. _github.com: http://github.com/boto/boto
.. _Online documentation: http://docs.pythonboto.org
.. _Python Cheese Shop: http://pypi.python.org/pypi/boto
.. _this: http://docs.pythonboto.org/en/latest/boto_config_tut.html
.. _gitflow: http://nvie.com/posts/a-successful-git-branching-model/
.. _neo: https://github.com/boto/boto/tree/neo
.. _boto-users Google Group: https://groups.google.com/forum/?fromgroups#!forum/boto-users


%prep
%setup -n %{pythonname}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
