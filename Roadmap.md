# Roadmap

(Okay, I need to say this. It was not a good decision on my part, to directly mirror js-bitswap, and its file structure [That was outright dumb] :sweat_smile: )  

##Important Components

TODO:
- [x] WantList
- [x] WantListEntry
- [ ] Message
- [ ] MessageEntry
- [ ] DecisionEngine
- [x] Ledger
- [ ] BlocksQueue (and BlocksQueueEntry?)
- [ ] WantManager
- [ ] MessageQueue (and MessageQueueEntry?)
- [ ] NetworkManager and interface (we can directly use libp2p here, or make some mock-up for the time being)
- [x] IPFSBlock

Later On:
1. Stats
2. Sessions

## Overall Working

#### Sending:
* __NetworkManager__ receives a __Message__, containing a __WantList__ from peer
* __DecisionEngine__ goes through __WantListEntries__ and checks if in local storage (py-datastore) and the __Ledger__
* For all matching blocks, creates a priority queue (__BlocksQueue__)
* __NetworkManager__ will send the __IPFSBlockss__ from the priority queue

#### Requesting:
* Gets a request from the user
* __WantManager__ manages requests and maintains them in a __MessageQueue__
* __NetworkManager__ sends the entries from the __MessageQueue__ in a __WantList__ to each peer

#### Getting blocks from peers:
* __NetworkManager__ gets a __Message__ containing blocks from a peer
* __WantManager__ handles this and stores the blocks in the __Ledger__ and local storage
* Announces this on the DHT (To be done later)

#### Stats:
To be done later. For now, we can treat all peers with equal priority or use just some simple metric.

#### Sessions:
To be done later

#### Finding Providers:
To be done later, after DHT

### Diagrams
Please refer to [the diagrams in docs](https://github.com/AliabbasMerchant/py-bitswap/tree/master/docs/diagrams)  
(Sorry for my hand-drawn py_architecture.jpeg :sweat_smile: )

#### Dependencies
Refer to [this](https://github.com/AliabbasMerchant/py-bitswap/tree/master/research/js_bitswap_inference.txt)

## Implementation
* Internal classes
* Interface between different classes
* Mock-up/connection to IPFS and lib-p2p
* Tests - Unit and Integration
* Any missing dependencies, if needed

---

_PS_: I have no prior industry experience, so please bear with my not-so-good architecting and project management skills. Any feedback on that would be highly appreciated and welcome.  

_PPS_: Just saying, I would love to be a part of the DHT and DAG implementation.
