# Certificate Authority

In this section we will show you how to setup and use a Certificate Authority

## Why do I need a Certificate Authority

A Certificate Authority (CA) is a great way to manage all your **internal** certificates.

When making your own Certificate Authority, you usually will have a self-signed root certificate.
This means that all devices that will use any of these certificates will have to have this root certificate installed - Don't worry. We can manage this!

A CA can have multiple purposes, some things you could do are:

* SSH Authentication
* SSH Host Validity
* HTTPS Certificates

## Sounds Cool! Where do I start

Start at the [setup](setup/) page