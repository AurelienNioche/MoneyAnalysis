# MoneyAnalysis

## Simulations

### General

Eg: 

Launch simulations with 3 goods for phase diagram 
    
    python main.py -n 3 -p -f

Launch simulations with 3 goods 'experiment-like'

    python main.py -n 3 -f
  
### Supplementary

Scripts related to supplementary section are 'simulation/supplementary_exploration.py' and 
'simulation/supplementary_exploitation.py'.

The former script aims at finding 20 combinations (this number is arbitrarily determined) of 10 set of cognitive parameters where the first 9 of them are homogeneous
(one alpha, beta and gamma same for all agents) and with significant results regarding the emergence of money, while
the last set of parameter (10th) is heterogeneous and composed of combinations of the previous homogeneous parameters (one set of different 
a set of alpha, beta, gamma potentially different for each agent) and with
non significant results (meaning that no good can be considered as a money). 
Indeed, it shows that some set of cog parameters may allow money emergence when they are homogeneously distributed, although the combinations 
of them distributed heterogeneously among agents may results in a non monetary system. These results 
may account for the hypothesis of cognitive heterogeneity among agents as a precluding factor of money emergence.

The latter script exploits those results (for the moment 20 batch of 10 set of cognitive parameters were selected
 and saved in supplementary.p file) by taking each set and varying specifically the set of heterogeneous parameters as well as the seed 
 used in simulations, in order to test its robustness.
 Currently, among the 20 batch, the 6th batch seems to be the more robust. On 100 trials, 25 trial (on average) were successful (
 meaning that varying the heterogeneous parameters set a hundred times returned significant results for the first 9 set of parameters
 and in contrary non-significant results in regards to the 10th set of parameters).

