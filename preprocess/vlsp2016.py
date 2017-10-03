from os.path import dirname, join
from underthesea_flow.reader.tagged_corpus import TaggedCorpus


def load_data(file):
    tagged_corpus = TaggedCorpus()
    tagged_corpus.load(file)
    sentences = tagged_corpus.sentences
    return sentences


def sample_data(n=200):
    tagged_corpus = TaggedCorpus()
    file = join(dirname(__file__), "corpus", "vlsp_chunk", "train.txt")
    tagged_corpus.load(file)
    sentences = tagged_corpus.sentences[:n]
    sample_corpus = TaggedCorpus(sentences)
    file = join(dirname(__file__), "corpus", "vlsp_chunk_sample", "train.txt")
    sample_corpus.save(file)


def preprocess_vlsp(sentences):
    def process_token(t):
        output = t[:-1]
        output[0] = t[0].replace("_", " ")
        return output

    def process_sentence(s):
        return [process_token(t) for t in s]

    return [process_sentence(s) for s in sentences]


def raw_to_corpus():
    for f in ["train.txt", "dev.txt", "test.txt"]:
        tagged_corpus = TaggedCorpus()
        input = join(dirname(dirname(__file__)), "raw", "vlsp2016", f)
        tagged_corpus.load(input)
        tagged_corpus.sentences = preprocess_vlsp(tagged_corpus.sentences)
        output = join(dirname(dirname(__file__)), "corpus", "vlsp2016", f)
        tagged_corpus.save(output)


def raw_to_sample_corpus():
    for f in ["train.txt", "dev.txt", "test.txt"]:
        tagged_corpus = TaggedCorpus()
        input = join(dirname(dirname(__file__)), "raw", "vlsp2016", f)
        tagged_corpus.load(input)
        tagged_corpus.sentences = preprocess_vlsp(tagged_corpus.sentences)[:100]
        output = join(dirname(dirname(__file__)), "corpus", "sample_vlsp_2016",
                      f)
        tagged_corpus.save(output)


if __name__ == '__main__':
    # raw_to_corpus()
    raw_to_sample_corpus()
    # sample_data()
    # file = join(dirname(__file__), "corpus", "vlsp_chunk", "train.txt")
    # load_data(file)
