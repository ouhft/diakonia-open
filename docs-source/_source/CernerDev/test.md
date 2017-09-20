# Cerner Test/Probe Environment

There are a lot of unknowns, assumptions, and false assertions that need to be confirmed when working in the Cerner Millennium environment. The basic aim of the pages and scripts here is to poke from the inside as much of the tech as possible to provide clues as to what is possible, what is working, and what has changed.

## MPages
Looking specifically at the MPages technology and environment, my working understanding (currently ranked as very minimal and entirely anecdotal) is that the PowerChart desktop application uses an 
 Internet Explorer instance (e.g. an iFrame within the app) to provide the rendering engine for HTML content. There is JS and CSS support (to an undefined degree, and with quirks) and we want to know as much about this from a pragmatic and definitive standpoint as possible (relying on what we're told or can read from training materials is insufficient at best and sophistry at worst).
    
