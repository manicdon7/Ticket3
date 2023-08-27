from django.shortcuts import render
from django.shortcuts import render
from web3 import Web3
import json
from django.core.serializers import serialize

# Create your views here.
def index(request):
    return render(request,"index.html")
def dashboard(request):
    return render(request,"dashboard.html")
def book(request):
    return render(request,"book.html")
def host(request):
    return render(request,"host.html")
def about(request):
    return render(request,"about.html")
def booking(request):
    return render(request,"booking.html")

web3 = Web3(Web3.HTTPProvider(
    'https://evm.ngd.network:32332'))

with open("templates/abi.json", "r") as abi_file:
    contract_abi = json.load(abi_file)

contract_address = '0xb07d0Af83889b79515009dD130eF7c14EEeF9a5B'

contract = web3.eth.contract(address=contract_address, abi=contract_abi)

def event_details(request, event_id):
    try:
        event_data = contract.functions.getEventDetails(event_id).call()

        event = {
            'name': event_data[0],
            'location': event_data[1],
            'date': event_data[2],
            'time': event_data[3],
            'total_tickets': event_data[4],
            'ticket_price': event_data[5]
        }

        return render(request, 'event_details.html', {'event': event})
    except Exception as e:
        error_message = str(e)
        return render(request, 'error.html', {'error_message': error_message})
