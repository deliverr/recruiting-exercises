
interface ProcessorResult {
  zipFrom: string;
  zipTo: string;
  cost: number;
  serviceLevel: string; // usps_priority
  
  percentDeliveredWithinOneDay: number;
  percentDeliveredWithinTwoDays: number;
  percentDeliveredWithinThreeDays: number;
}