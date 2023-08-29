def minChunkRequired(totalPacket, uploadedChunks):
    n = len(uploadedChunks)
    num_chunks = []
    head, tail = 0, 0
    for i in range(n):
        tail = uploadedChunks[i][0]
        if tail - head -1 > 0:
            num_chunks.append(chunkDivided(tail-head-1))
        head = uploadedChunks[i][1]
    tail = totalPacket+1
    if tail - head -1 > 0:
        num_chunks.append(chunkDivided(tail-head-1))
    return sum(num_chunks)

def chunkDivided(num):
    cnt = 0
    while num:
        cnt += num & 1
        num >> 1
    return cnt
