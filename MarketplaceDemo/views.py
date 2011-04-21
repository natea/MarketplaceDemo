# Copyright 2011 HubSpot, Inc.
#
#   Licensed under the Apache License, Version 2.0 (the 
# "License"); you may not use this file except in compliance 
# with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, 
# software distributed under the License is distributed on an 
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, 
# either express or implied.  See the License for the specific 
# language governing permissions and limitations under the 
# License.

"""
Django views for the Marketplace Demo app.
"""

import base64
import hashlib
import hmac

from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

def params_get(request):
    ctx = { 'GET' : request.GET,
            'POST' : request.POST,
            'META' : request.META }
    return render_to_response('params.html', ctx)

def form(request):
    if request.method == 'GET':
        return render_to_response('form.html', RequestContext(request, {}))
    else:
        # Handle the form
        ctx = { 'GET' : request.GET,
                'POST' : request.POST,
                'META' : request.META }
        return render_to_response('params.html', ctx)
        
    
def form_plus_redir(request):
    if request.method == 'GET':
        return render_to_response('form_plus_redir.html', RequestContext(request, {}))
    else:
        return redirect("/marketplacetest/redir_dest")

        
    
def verify_signed_request(request):
    signed_req = request.GET["hubspot.marketplace.signature"]
    secret = "(your HubSpot API secret"
    payload = get_verified_payload(signed_req, secret)
    return render_to_response("verified.html", { 'payload' : payload })

def get_verified_payload(signed_request, secret):
    """
    Return the payload from the signed request, or raise an informative
    exception if it fails to decode properly
    """
    if not signed_request:
        raise Exception("No signed request passed in")

    signed_request = str(signed_request) # convert from unicode
    
    if "." not in signed_request:
        raise Exception("improperly formed signed request -- missing '.'")
    
    signature, payload = signed_request.split(".",1)
    if not signature:
        raise Exception("No signature found in signed request")

    decoded_signature = decode(signature)
    decoded_payload = decode(payload)

    expected_signature = hmac.new(secret, decoded_payload, hashlib.sha1).digest()
    
    if(expected_signature != decoded_signature):
        raise Exception("Signature doesn't match expectation")
    
    return decoded_payload


def decode(s):
    return base64.urlsafe_b64decode(s + '=' * (4 - len(s) % 4))
