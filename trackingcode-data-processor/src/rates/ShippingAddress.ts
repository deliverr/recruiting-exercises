
export interface ShippingAddress {
  readonly name: string;
  readonly company?: string;
  readonly street1: string;
  readonly street2?: string;
  readonly city: string;
  readonly zip: string;
  readonly state: string;
  readonly country: string; // the standard ISO-3166-1 country code
  readonly phone?: string;
  readonly email?: string;
  readonly isResidential?: boolean; // we can get this info from Shippo
}
