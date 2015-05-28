# profile

InputProfile

# service.adaptation.effector

# service.adaptation.probes

# service.adaptation.probes.interfaces

# service.atomic

# service.auxilliary

# service.client

# service.composite

# service.provider

# service.provider.activemq

# service.provider.rsp

# service.registry

# service.utility

# service.workflow

# service.workflow.ast

# taskgraph

# tools



adaptation
provider
workflow



services; atomic services, composite services

|-------------------------------------------------------------------|
|                     External Systems                              |
|-------------------------------------------------------------------|

|-------------------------------------------------------------------|
| Services Layer                                                    |
|                                                                   |
| > Atomic Service < > Service Description <                        |
|-------------------------------------------------------------------|

|-------------------------------------------------------------------|
| Business Layer                                                    |
|                                                                   |
| > Service Registry                                              < |
|                                                                   |
| > Service Client < > Composite Service <                          |
|-------------------------------------------------------------------|

Atomic services har en egen funktionalitet som inte är beroende av andra services.

En service description innehåller information om en service. Bland annat namn,
a list of supported operations, address.

Composite services är andra services ihopkopplade baserat på ett workflow, som
förklarar hur services ska how to compose them.
En workflow engine används för att execute the workflow.

Service registry används för att registrera och lookup services med hjälp av en
service description.






Atomic services provide single domain functionality by means of operations that
do not depend on other services.

Composite services are composed of other services based on a workflow. The
workflow states how to compose other services.

ReSeP provides a workflow engine, which is used by composite services to execute
the workflow.

Service registry is a special kind of atomic service provided by ReSeP. It
provides the functionality to register other services. Service registry also
provides the functionality to lookup other services.

Services are registered to the service registry usinng a service description.
A service description contains the name of the service, a list of operations
supported by a service, an address, among other things.

ReSeP also provides support to use composite services, i.e., service clients.
When a service client invokes a composite service, the composite service looks
for services specified in the workflow through the service registry. The
service registry receives service and operation names and returns a list of
service descriptions.
