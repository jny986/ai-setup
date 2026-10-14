# Laravel Examples

Examples use Pest; the same points hold in PHPUnit.

## Good test: observable behavior

```php
// GOOD: Tests observable behavior
test('user can checkout with valid cart', function () {
    $cart = Cart::factory()->create();
    $cart->add($product);
    $result = Checkout::process($cart, $paymentMethod);
    expect($result->status)->toBe('confirmed');
});
```

## Bad: implementation-coupled

```php
use function Pest\mock;

// BAD: Tests implementation details
test('checkout calls payment service process', function () {
    mock(PaymentService::class)
        ->shouldReceive('process')
        ->once()
        ->with($cart->total);

    Checkout::process($cart, $payment);
});
```

```php
// BAD: Bypasses interface to verify
test('createUser saves to database', function () {
    createUser(['name' => 'Alice']);
    $row = DB::table('users')->where('name', 'Alice')->first();
    expect($row)->not->toBeNull();
});

// GOOD: Verifies through interface
test('createUser makes user retrievable', function () {
    $user = createUser(['name' => 'Alice']);
    $retrieved = getUser($user->id);
    expect($retrieved->name)->toBe('Alice');
});
```

## Bad: tautological (expected value recomputes the code's own logic)

```php
// BAD: Expected value is recomputed the way the code computes it
test('calculateTotal sums line items', function () {
    $items = [['price' => 10], ['price' => 5]];
    $expected = array_sum(array_column($items, 'price'));
    expect(calculateTotal($items))->toBe($expected);
});

// GOOD: Expected value is an independent, known literal
test('calculateTotal sums line items', function () {
    expect(calculateTotal([['price' => 10], ['price' => 5]]))->toBe(15);
});
```

## Mocking: dependency injection

```php
// Easy to mock: bound via the container, swappable in tests
class ProcessPayment
{
    public function __construct(private PaymentClient $paymentClient) {}

    public function handle(Order $order)
    {
        return $this->paymentClient->charge($order->total);
    }
}

// Hard to mock: constructs its own dependency internally
class ProcessPayment
{
    public function handle(Order $order)
    {
        $client = new StripeClient(config('services.stripe.key'));
        return $client->charge($order->total);
    }
}
```

## Mocking: SDK-style interfaces

```php
// GOOD: Each method is independently mockable/fakeable
class Api
{
    public function getUser(int $id) { /* ... */ }
    public function getOrders(int $userId) { /* ... */ }
    public function createOrder(array $data) { /* ... */ }
}

// BAD: Mocking requires conditional logic inside the mock
class Api
{
    public function call(string $endpoint, array $options = []) { /* ... */ }
}
```
