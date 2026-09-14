import sys, math

# Cross-entropy loss for one position:
#   loss = -z[correct] + logsumexp(z)
# Use the (z - max(z)) trick for numerical stability.

for raw in sys.stdin:
    line = raw.rstrip("\n").strip()
    if not line or not line.startswith("XE "):
        continue
    # XE <correct_id>; <comma-separated logits>
    # TODO: parse, compute logsumexp, emit 4-decimal loss.
    true_id = int(line[3])
    logits = line[6:].split(',')
    for i in range(len(logits)):
        logits[i] = float(logits[i])
    logsumexp = 0
    for zi in logits:
        logsumexp = logsumexp + math.exp(zi)
    logsumexp = math.log(logsumexp)
print(round(logsumexp - logits[true_id],4))
