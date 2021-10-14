mkdir -p modelYelp

dir="http://people.csail.mit.edu/tianxiao/language-style-transfer/model/"

wget ${dir}yelp.d100.emb.txt -P modelYelp/
wget ${dir}yelp.vocab -P modelYelp/
wget ${dir}model.data-00000-of-00001 -P modelYelp/
wget ${dir}model.index -P modelYelp/
wget ${dir}model.meta -P modelYelp/
