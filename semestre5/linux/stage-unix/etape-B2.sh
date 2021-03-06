#!/bin/bash

# RedHat bug with base64 -d => use -i as a workaround
# https://bugzilla.redhat.com/show_bug.cgi?id=719317
bash -c "$(base64 -di <<EOF
IyEvYmluL2Jhc2gKCnA9JycKY2F0IDw8IE5FU1RFREVPRgpFbnRyZXogY2ktZGVzc291cyBsZSBt
b3QgZGUgcGFzc2UuCgpDZSBtb3QgZGUgcGFzc2Ugdm91cyBlc3QgZG9ubsOpIGRhbnMgbGUgZ3Vp
ZGUgwqvCoEluaXRpYXRpb24gw6AgVW5peCwKTCdlbnZpcm9ubmVtZW50IGRlIHRyYXZhaWwgw6Ag
bCdFbnNpbWFnwqDCuywgY2hhcGl0cmUgNC4gU2kgdm91cyBuJ2F2ZXoKcGFzIGVuY29yZSBsdSBs
ZSBndWlkZSBqdXNxdWUgbMOgLCBpbCBlc3QgdGVtcHMgZCdhdmFuY2VyIHN1ciBsYQpsZWN0dXJl
IGRlIGNlIGRvY3VtZW50LCB2b3VzIGNvbnRpbnVlcmV6IGxlIGpldSBkZSBwaXN0ZSBhcHLDqHMu
Ck5FU1RFREVPRgplY2hvCgp3aGlsZSBbICIkcCIgIT0gamV1MnBpc3RlIF07IGRvCiAgICBwcmlu
dGYgJyVzJyAiTW90IGRlIHBhc3NlIDogIgogICAgcmVhZCBwCiAgICBpZiBbIC16ICIkcCIgXTsg
dGhlbgogICAgICAgIGVjaG8gIkF1IHJldm9pciIKICAgICAgICBleGl0CiAgICBmaQpkb25lCgpl
Y2hvCgpjYXQgPDwgTkVTVEVERU9GClRyw6hzIGJpZW4uCgpMJ2V0YXBlIHN1aXZhbnRlIHNlIHRy
b3V2ZSBkYW5zIGxlIGZpY2hpZXIuCmh0dHA6Ly9saWctZW5zZWlnbmVtZW50LmltYWcuZnIvamV1
LWRlLXBpc3RlL2V0YXBlLUMxLnRleAoKQ2V0dGUgZm9pcy1jaSwgYydlc3QgdW4gZmljaGllciBM
YVRlWC4gTGFUZVggZXN0IHVuIGZvcm1hdCBkZSBmaWNoaWVyCnF1aSBwZXJtZXQgZGUgZmFpcmUg
ZGUgam9saXMgZG9jdW1lbnRzIGF2ZWMgdW5lIG1pc2UgZW4gcGFnZQphdXRvbWF0aXF1ZS4gVm91
cyBwb3V2ZXogY29tcGlsZXIgY2UgZmljaGllciBhdmVjIGxhIGNvbW1hbmRlCgogIHBkZmxhdGV4
IGV0YXBlLUMxLnRleAoKcG91ciBvYnRlbmlyIHVuIGZpY2hpZXIgUERGLCBxdWUgdm91cyBvdXZy
aXJleiBlbnN1aXRlIGF2ZWMgbGUKbG9naWNpZWwgYXBwcm9wcmllLgpORVNURURFT0YK
EOF
)"
