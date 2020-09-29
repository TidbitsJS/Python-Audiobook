import slate3k as slate

with open('whiteNight.pdf', 'rb') as f:
    extractedText = slate.PDF(f)
print(extractedText)