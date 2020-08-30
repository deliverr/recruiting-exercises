
/* tslint:disable */
declare module "shippo" {
  
    namespace Shippo {
      class AddressApi {
        public create(address: any): Promise<AddressResponse>;
      }
  
      class AddressRequest extends Address {
        public validate: boolean;
      }
  
      class AddressResponse extends Address {
        public validation_results: { is_valid: boolean, messages: [object] };
      }
  
      class Address { // pretty standard format
        public name: string;
        public street1: string;
        public street2?: string;
        public city: string;
        public state: string;
        public zip: string;
        public country: string;
        public phone?: string;
        public email?: string;
        public is_residential?: boolean;
      }
  
      type MassUnit = "lb" | "kg";
      type DistanceUnit = "in" | "cm";
  
  
      type RateAttribute = "CHEAPEST" | "FASTEST" | "BESTVALUE";
  
      class Rate {
        public "object_created": Date;
        public "object_id": string;
        public "object_owner": string;
        public attributes: RateAttribute[];
        public "shipment": string;
        public "amount_local": string;
        public "currency_local": string;
        public "amount": string;
        public "currency": string;
        public "provider": string;
        public "provider_image_75": string;
        public "provider_image_200": string;
        public "servicelevel": {
          "name": string
          "token": string
          "terms": string,
        };
        public "estimated_days": number;
        public "duration_terms": string;
        public "carrier_account": string;
        public "zone": string;
        public "messages": any[];
        public "test": boolean;
      }
  
      export class Shipment {
        public address_from: Address;
        public address_to: Address;
        public parcels: Parcel[];
        public rates: Rate[];
      }
  
      export class ShipmentApi {
        public create(params: {
          address_from: Address, address_to: Address,
          parcels: Parcel[], async: boolean
        }): Promise<Shipment>;
      }
  
      export interface Parcel {
        length?: number;
        width?: number;
        height?: number;
        weight: number;
        distance_unit: DistanceUnit;
        mass_unit: MassUnit;
      }
  
      class TrackingApi {
        public get_status(carrier: string, trackingCode: string): Promise<TrackingInfo>
        public create(data: {carrier: string, tracking_number: string, metadata?: string}): Promise<object>
      }
  
      class TrackingInfo {
        carrier: string;
        tracking_number: string;
        address_from: Partial<Address>
        address_to: Partial<Address>
        eta: Date;
        original_eta: Date;
        service_level: {
          token: string,
          name: string,
        };
        metadata: string;
        tracking_status: TrackingItem;
        tracking_history: TrackingItem[]
      }

      class TrackingItem {
        object_created: Date;
        object_id: string;
        status: "TRANSIT" | "DELIVERED" | "UNKNOWN" | "FAILURE" | "RETURNED";
        status_details: string;
        status_date: Date;
        location: Partial<Address>
      }
    }
  
    function Shippo(key: string | undefined): {
      address: Shippo.AddressApi
      shipment: Shippo.ShipmentApi,
      track: Shippo.TrackingApi,
    };
  
    export = Shippo;
  }