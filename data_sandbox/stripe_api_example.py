import stripe
stripe.api_key = "sk_test_BQokikJOvBiI2HlWgH4olfQ2"

stripe.Charge.create(
  amount=400,
  currency="usd",
  card={
    "number": '4242424242424242',
    "exp_month": 12,
    "exp_year": 2015,
    "cvc": '123'
  },
  description="Charge for test@example.com"
)