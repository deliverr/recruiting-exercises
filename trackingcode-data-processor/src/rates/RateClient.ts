import * as Shippo from "shippo";
import { ShippingAddress } from "./ShippingAddress";

const shippo = Shippo("shippo_test_ff55fcc82742b5e5916e94a7ff574c4464b917cc");

export class RateClient {


  public async getTrackingInfo(carrier: string, trackingNumber: string): Promise<Shippo.TrackingInfo> {
    return shippo.track.get_status(carrier, trackingNumber);
  }

  public async getRates(fromAddress: ShippingAddress, toAddress: ShippingAddress,
                                   parcels: Shippo.Parcel[]): Promise<Shippo.Rate[]> {

    const shipment = await shippo.shipment.create({
      address_from: fromAddress,
      address_to: toAddress,
      parcels,
      async: false,
    });

    return shipment.rates;
  }
}
