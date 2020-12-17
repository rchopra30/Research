import tensorflow as tf
from transformers import TFGPT2LMHeadModel, GPT2Tokenizer
from transformers import XLNetTokenizer, XLNetLMHeadModel


tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
# tokenizer = XLNetTokenizer.from_pretrained('xlnet-large-cased')
text = open("output_stereo.txt", "w")

# add the EOS token as PAD token to avoid warnings
model = TFGPT2LMHeadModel.from_pretrained(
    "gpt2", pad_token_id=tokenizer.eos_token_id)
# model = XLNetLMHeadModel.from_pretrained('xlnet-large-cased')

count = 0
with open("stereo_data.txt", "r") as data:
    for line in data:
        count += 1
        # skip every other line since duplicate prompt in one data file
        if count < 0:
            continue

        input_ids = tokenizer.encode(line.rstrip(), return_tensors='tf')

        # make set to get 3 unique strings
        out = set()
        while len(out) < 3:
            # generate output
            beam_output = model.generate(
                input_ids,
                max_length=100,
                num_beams=25,
                no_repeat_ngram_size=2,
                num_return_sequences=3,
                early_stopping=False,
                do_sample=True
            )

            for b in beam_output:
                #print('b' + tokenizer.decode(b, skip_special_tokens=True))
                t = tokenizer.decode(b, skip_special_tokens=True).split(line)
                t = t[len(t) - 1]
                #print('t: ' + t)
                if len(out) < 3:
                    out.add(t)

        text.write(line.rstrip())
        print(line.rstrip())
        for t in out:
            text.write(t.rstrip())
            print(t.rstrip())
        text.write(' \n')

print('Done')
