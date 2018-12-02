# Collaborative Filtering Project

## Data pre-processing
Before feeding to the network, the cell-genes data is pre-processed using the process.m procedure in (https://github.com/aanchalMongia/McImpute_scRNAseq).

## Result Reproducability

We were able to reproduce results by He et al. (https://github.com/duxy-me/ConvNCF) on Yelp dataset.

![alt text](https://user-images.githubusercontent.com/16076960/49336939-33577480-f631-11e8-8672-491e45ac88c4.png)


Metric | Highest value in He et al.'s experiments | Highest value in our Experiments |
:---: | :---: | :---: 
HR@10 | 0.31  | 0.31 
NDCG@10  | 0.162  | 0.16

## References 
1. Paul Blakeley, Norah ME Fogarty, Ignacio Del Valle, Sissy E Wamaitha, Tim Xi- aoming Hu, Kay Elder, Philip Snell, Leila Christie, Paul Robson, and Kathy K Niakan. Defining the three cell lineages of the human blastocyst by single-cell rna-seq. Development, pages dev–123547, 2015.
2. Spyros Darmanis, Steven A Sloan, Ye Zhang, Martin Enge, Christine Caneda, Lawrence M Shuer, Melanie G Hayden Gephart, Ben A Barres, and Stephen R Quake. A survey of human brain transcriptome diversity at the single cell level. Proceedings of the National Academy of Sciences, 112(23):7285–7290, 2015.
3. F Maxwell Harper and Joseph A Konstan. The movielens datasets: History and context. Acm transactions on interactive intelligent systems (tiis), 5(4):19, 2016.
4. Xiangnan He, Xiaoyu Du, Xiang Wang, Feng Tian, Jinhui Tang, and Tat- Seng Chua. Outer product-based neural collaborative filtering. arXiv preprint arXiv:1808.03912, 2018.
5. Xiangnan He, Lizi Liao, Hanwang Zhang, Liqiang Nie, Xia Hu, and Tat-Seng Chua. Neural collaborative filtering. In Proceedings of the 26th International Conference on World Wide Web, pages 173–182. International World Wide Web Conferences Steering Committee, 2017.
6. Aleksandra A Kolodziejczyk, Jong Kyoung Kim, Jason CH Tsang, Tomislav Ilicic, Johan Henriksson, Kedar N Natarajan, Alex C Tuck, Xuefei Gao, Marc Bu ̈hler, Pentao Liu, et al. Single cell rna-sequencing of pluripotent states unlocks modular transcriptional variation. Cell stem cell, 17(4):471–485, 2015.
7. Wei Vivian Li and Jingyi Jessica Li. scimpute: accurate and robust imputation for single cell rna-seq data. BioRxiv, page 141598, 2017.
8. Aanchal Mongia, Debarka Sengupta, and Angshul Majumdar. Mcimpute: Matrix completion based imputation for single cell rna-seq data. bioRxiv, page 361980, 2018.
9. SteffenRendle,ChristophFreudenthaler,ZenoGantner,andLarsSchmidt-Thieme. Bpr: Bayesian personalized ranking from implicit feedback. In Proceedings of the twenty-fifth conference on uncertainty in artificial intelligence, pages 452–461. AUAI Press, 2009.
10. Fuchou Tang, Catalin Barbacioru, Yangzhou Wang, Ellen Nordman, Clarence Lee, Nanlan Xu, Xiaohui Wang, John Bodeau, Brian B Tuch, Asim Siddiqui, et al. mrna-seq whole-transcriptome analysis of a single cell. Nature methods, 6(5):377, 2009.
11. Dmitry Usoskin, Alessandro Furlan, Saiful Islam, Hind Abdo, Peter L ̈onnerberg, Daohua Lou, Jens Hjerling-Leffler, Jesper Haeggstro ̈m, Olga Kharchenko, Peter V Kharchenko, et al. Unbiased classification of sensory neuron types by large-scale single-cell rna sequencing. Nature neuroscience, 18(1):145, 2015.
12. Liying Yan, Mingyu Yang, Hongshan Guo, Lu Yang, Jun Wu, Rong Li, Ping Liu, Ying Lian, Xiaoying Zheng, Jie Yan, et al. Single-cell rna-seq profiling of human preimplantation embryos and embryonic stem cells. Nature structural & molecular biology, 20(9):1131, 2013.
13. Amit Zeisel, Ana B Mun ̃oz-Manchado, Simone Codeluppi, Peter Lo ̈nnerberg, Gioele La Manno, Anna Jur ́eus, Sueli Marques, Hermany Munguba, Liqun He, Christer Betsholtz, et al. Cell types in the mouse cortex and hippocampus re- vealed by single-cell rna-seq. Science, 347(6226):1138–1142, 2015.
14. Grace XY Zheng, Jessica M Terry, Phillip Belgrader, Paul Ryvkin, Zachary W Bent, Ryan Wilson, Solongo B Ziraldo, Tobias D Wheeler, Geoff P McDermott,
Title Suppressed Due to Excessive Length 13
Junjie Zhu, et al. Massively parallel digital transcriptional profiling of single cells. Nature communications, 8:14049, 2017.
