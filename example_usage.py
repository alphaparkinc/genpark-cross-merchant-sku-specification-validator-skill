from client import CrossMerchantSkuSpecificationValidatorClient

def main():
    client = CrossMerchantSkuSpecificationValidatorClient()
    res = client.validate_sku_compatibility('NVME_PCIE4_4TB', 'ThinkPad P1 Gen 6', 65)
    print('SKU Specification Validator: ' + res['validation_report_id'] + ' (' + res['sku_identifier'] + ')')
    print('Compatible: ' + str(res['hardware_compatibility_verified']) + ' | Power OK: ' + str(res['power_delivery_sufficient']))
    print('Warranty: ' + str(res['manufacturer_warranty_months']) + ' months | Conflict: ' + str(res['merchant_spec_conflict_detected']))
    print('Dossier: ' + res['specification_audit_dossier_url'])

if __name__ == '__main__':
    main()
