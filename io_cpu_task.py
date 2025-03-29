import asyncio
import time
import aiohttp
import multiprocessing

async def fetch_cart(session, cart_id):
    url = f"https://dummyjson.com/carts/{cart_id}"
    await asyncio.sleep(cart_id) # Simulate network delay for each cart
    async with session.get(url) as response:
        return await response.json()

def calculate_cart_total_price(cart):
    products = cart["products"]
    time.sleep(cart["id"]) # Simulate CPU-heavy work for each cart
    return cart["id"], sum(product["total"] for product in products)

async def main():
    start_time = time.time()
    card_ids = [1, 2, 3, 4, 5]
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_cart(session, url) for url in card_ids]
        responses = await asyncio.gather(*tasks)
        fetching_elapsed_time = time.time() - start_time
        print("All carts fetched in {} seconds, instead of ~{}".format(fetching_elapsed_time, sum(card_ids)))

    # Use multi-processing for CPU-intensive processing
    with multiprocessing.Pool(processes=5) as pool:
        results = pool.map(calculate_cart_total_price, responses)

    print("Total price of all carts:", sum(result[1] for result in results))

    processing_elapsed_time = time.time() - start_time - fetching_elapsed_time
    print("Calculation done in {} seconds instead of ~{}".format(processing_elapsed_time, sum(card_ids)))

    total_elapsed_time = time.time() - start_time
    print("Total elapsed time: {} seconds, instead of ~{}".format(total_elapsed_time, sum(card_ids)*2))

asyncio.run(main())