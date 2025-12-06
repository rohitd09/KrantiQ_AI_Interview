import time
import threading
from collections import defaultdict
from typing import Optional

class TokenBucketRateLimiter:
    
    def __init__(self, capacity: int = 20, refill_rate: float = 20//60.0):
 
        self.capacity = capacity
        self.refill_rate = refill_rate 
        
        # Stores user bucket state: {user_id: {'tokens': float, 'last_refill': float}}
        self.user_buckets = defaultdict(lambda: {
            'tokens': capacity,
            'last_refill': time.time(),
        })
        self.lock = threading.Lock()

    def _refill_tokens(self, user_id: str, now: float) -> None:
        bucket = self.user_buckets[user_id]
        
        elapsed = now - bucket['last_refill'] # Calculate time elapsed since the last refill
        new_tokens = elapsed * self.refill_rate
        bucket['tokens'] = min(self.capacity, bucket['tokens'] + new_tokens)
        
        bucket['last_refill'] = now

    def allow_request(self, user_id: str) -> bool:
        with self.lock:
            now = time.time()
            
            # 1. Refill the tokens before checking
            self._refill_tokens(user_id, now)
            
            bucket = self.user_buckets[user_id]
            
            # 2. Check for available tokens and consume one if available
            if bucket['tokens'] >= 1.0:
                bucket['tokens'] -= 1.0
                return True
            else:
                return False

def example_usage():
    # 20 requests max burst, refilling at 20 requests per 60 seconds (1 token every 3 seconds)
    limiter = TokenBucketRateLimiter()
    
    user_id = "rohit_user"
    
    print("Testing Token Bucket Rate Limiter (20 req/min limit)...")
    print("-------------------------------------------------------")
    
    start_time = time.time()
    
    # Burst (First 20 requests should pass instantly)
    print("Phase 1: Testing initial burst...")
    for i in range(25):
        allowed = limiter.allow_request(user_id)
        current_time = time.time()
        bucket = limiter.user_buckets[user_id]
        
        status = 'ALLOWED' if allowed else 'BLOCKED'
        
        # Print status and tokens remaining
        print(f"[{current_time - start_time:5.2f}s] Req {i+1:2}: {status} | Tokens: {bucket['tokens']:5.2f}")
        
        if i == 19 and allowed:
            print("\n    *** BURST LIMIT OF 20 REACHED ***\n")
            
        # Introduce a small delay to simulate processing time, but quick enough for a burst
        time.sleep(0.5) 


if __name__ == "__main__":
    example_usage()