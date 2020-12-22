import tensorflow as tf
from transformers import TFGPT2LMHeadModel, GPT2Tokenizer
import json

# use the gpt2 model
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = TFGPT2LMHeadModel.from_pretrained(
    "gpt2", pad_token_id=tokenizer.eos_token_id)

# output file
# make sure to change when running code again because it will overwrite the previous file
text = open("output_stereo2.txt", "w")

# load the stereoset data
with open('dev.json') as d:
    data = json.load(d)

    # using the intersentence data rather than the intrasentence
    for s in data['data']['intersentence']:
        # get the gender biased data
        if(s['bias_type'] == 'gender'):
            input_ids = tokenizer.encode(
                s['context'].rstrip(), return_tensors='tf')
            # debug statements to print context and target to console
            # print('Context is:  ' + s['context'])
            # print('Target is:  ' + s['target'])

            # write context and target to file
            text.write('Context is:  ' + s['context'] + '\n')
            text.write('Target is:  ' + s['target'] + '\n')

            # make set to get 3 unique strings
            out = set()
            while len(out) < 3:
                # generate output
                beam_output = model.generate(
                    input_ids,
                    max_length=100,
                    num_beams=25,
                    no_repeat_ngram_size=2,
                    num_return_sequences=10,
                    early_stopping=False,
                    do_sample=True
                )

                for b in beam_output:
                    t = tokenizer.decode(
                        b, skip_special_tokens=True).splitlines()

                    # debug the output
                    # print(t[len(t) - 1])

                    if len(out) < 3:
                        out.add(t[len(t) - 1])

                # just making sure that out doesn't contain the input
                out.discard(s['context'].rstrip())

                # print the set of the outputs
                # print('out')
                # print(out)

                # write outputs to file
                text.write('Results \n')
                for o in out:
                    text.write(o + '\n')
                text.write('\n')
