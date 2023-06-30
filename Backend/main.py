from flask import Flask, request
from manager import create



app = Flask(__name__)

@app.route('/bot/comprar', methods=['POST'])
def compra():
    data = request.json

    # Extract relevant information from the JSON
    order_id = data.get('order_id')
    order_ref = data.get('order_ref')
    order_status = data.get('order_status')
    payment_method = data.get('payment_method')
    store_id = data.get('store_id')
    payment_merchant_id = data.get('payment_merchant_id')
    installments = data.get('installments')
    card_type = data.get('card_type')
    card_last4digits = data.get('card_last4digits')
    card_rejection_reason = data.get('card_rejection_reason')
    pix_code = data.get('pix_code')
    pix_expiration = data.get('pix_expiration')
    boleto_URL = data.get('boleto_URL')
    sale_type = data.get('sale_type')
    created_at = data.get('created_at')
    updated_at = data.get('updated_at')

    product_id = data['Product']['product_id']
    product_name = data['Product']['product_name']

    full_name = data['Customer']['full_name']
    email = data['Customer']['email']
    mobile = data['Customer']['mobile']
    CPF = data['Customer']['CPF']
    ip = data['Customer']['ip']

    charge_amount = data['Commissions']['charge_amount']
    product_base_price = data['Commissions']['product_base_price']
    kiwify_fee = data['Commissions']['kiwify_fee']

    commissioned_stores = data['Commissions']['commissioned_stores']
    commission_store_id = commissioned_stores[0]['id']
    commission_type = commissioned_stores[0]['type']
    commission_custom_name = commissioned_stores[0]['custom_name']
    commission_email = commissioned_stores[0]['email']
    commission_value = commissioned_stores[0]['value']

    my_commission = data['Commissions']['my_commission']

    src = data['TrackingParameters']['src']
    sck = data['TrackingParameters']['sck']
    utm_source = data['TrackingParameters']['utm_source']
    utm_medium = data['TrackingParameters']['utm_medium']
    utm_campaign = data['TrackingParameters']['utm_campaign']
    utm_content = data['TrackingParameters']['utm_content']
    utm_term = data['TrackingParameters']['utm_term']

    subscription_id = data['subscription_id']

    access_url = data.get('access_url')

    # Process the extracted data as per your requirements
    # ... user = create.user(create,client_cel=mobile, client_name=full_name)
    print(data)
    return data

@app.route('/bot/atrasar', methods=['POST'] )
def atrasar():
    data = request.json
    mobile = data['Customer']['mobile']

@app.route('/bot/cancelar', methods=['POST'] )
def cancelar():
    data = request.json


@app.route('/bot/renovar', methods=['POST'] )
def renovar():
    data = request.json


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)