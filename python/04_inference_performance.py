baseline = 40
optimized = 50

gain = optimized - baseline
improvement = (gain / baseline) * 100
speedup = optimized / baseline

print("Throughput Gain:", gain)
print("Improvement:", improvement)
print("Speedup:",speedup)