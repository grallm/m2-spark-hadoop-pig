#!/usr/bin/python
import datetime
from org.apache.pig.scripting import *

INIT = Pig.compile("""
A = LOAD '$input' using PigStorage(' ') as (url:chararray, p:chararray, link:chararray);
B = GROUP A by url;                                                                                  
C = foreach B generate group as url, 1 as pagerank, A.link as links;                                 
STORE C into '$docs_in';
""")

UPDATE = Pig.compile("""
-- PR(A) = (1-d) + d (PR(T1)/C(T1) + ... + PR(Tn)/C(Tn))

previous_pagerank = 
    LOAD '$docs_in' 
    USING PigStorage('\t') 
    AS ( url: chararray, pagerank: float, links:{ link: ( url: chararray ) } );

outbound_pagerank =  
    FOREACH previous_pagerank 
    GENERATE 
        pagerank / COUNT ( links ) AS pagerank, 
        FLATTEN ( links ) AS to_url;

new_pagerank = 
    FOREACH 
        ( COGROUP outbound_pagerank BY to_url, previous_pagerank BY url INNER )
    GENERATE 
        group AS url, 
        ( 1 - $d ) + $d * SUM ( outbound_pagerank.pagerank ) AS pagerank, 
        FLATTEN ( previous_pagerank.links ) AS links;

STORE new_pagerank
    INTO '$docs_out' 
    USING PigStorage('\t');
""")

time_start = datetime.datetime.now()
params = {
    'd': '0.85',
    'docs_in': "gs://spark-365112/out/pagerank_data_simple",
    'input': 'gs://public_lddm_data/page_links_en.nt.bz2'
}

stats = INIT.bind(params).runSingle()
if not stats.isSuccessful():
      raise 'failed initialization'  # type: ignore

for i in range(3):
   out = "gs://spark-365112/out/pagerank_data_" + str(i + 1)
   params["docs_out"] = out
   Pig.fs("rmr " + out)
   stats = UPDATE.bind(params).runSingle()
   if not stats.isSuccessful():
      raise 'failed'
   params["docs_in"] = out
print("DURATION : " + str((datetime.datetime.now() - time_start).total_seconds()))
