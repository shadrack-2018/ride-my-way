# models file
import jwt
import datetime
import os

ride_offers={}

users={}
join_request={}

class Rides:
    """methods for Rides class."""
    @staticmethod
    def get_ride_offers():
        output = []
        for ride_id in ride_offers:

            data={}
            data['ride_id']=ride_id
            data['from']=ride_offers[ride_id]["from"]
            data['to']=ride_offers[ride_id]["to"]
            data['time']=ride_offers[ride_id]["time"]
            data['status']=ride_offers[ride_id]["status"]
            data['startpoint']=ride_offers[ride_id]["startpoint"]
            data['cost']=ride_offers[ride_id]["cost"]

            output.append(data)
        return output

    def get_ride_offer(self, ride_id):
        if ride_id not in ride_offers:
            return {"msg": "Ride id does not exist"}

        ride_offer=[ride_offer for ride_offer in ride_offers if ride_offer['ride_id']==ride_id]
        return jsonify(ride_offer)

    def create_ride_offer(origin, to, time, startpoint, cost, driver_id):
        if(len(ride_offers)==0):
            ride_id=1
        else:
            ride_id=ride_offers[-1]['ride_id']+1
        new_ride = {
        'ride_id': ride_id,
        'from': origin,
        'to': to,
        'time': time,
        'status': 1,
        'startpoint': startpoint,
        'cost': cost,
        'driver_id': driver_id
        }
        ride_offers.append(new_ride)
        return jsonify({'new_ride': new_ride, 'msg': 'new ride successfully added'})

    def join_request(self, ride_id, pickpoint, contact):
        ride_offer=[ride_offer for ride_offer in ride_offers if ride_offer['ride_id']==ride_id]
        if(ride_offer[0]['status']==1):
            if(len(join_requests)==0):
                join_id=1
            else:
                join_id=join_requests[-1]['join_id']+1
            join_request={
            'join_id': join_id,
            'ride': ride_id,
            'status': 1,
            'pickpoint': pickpoint,
            'contact': contact
            }
            join_requests.append(join_request)
        return jsonify({'join_request': join_request, 'msg': 'You have requested to join'}), 201

    #def accept_request(self, join_id)
        
