
# 📝 Publications 

## Preprints all field
--  **"Adaptive Path-Planning for Autonomous Robots: A UCH-Enhanced Q-Learning Approach"**  
Wei Liu,Ruiyang Wang,<span style="color:darkblue">**Haonan Wang**</span>, Guangwei Liu.\
[***under review***]Advances in Artificial Intelligence and Machine Learning, 2025. [[pdf]](https://arxiv.org/abs/2501.05411),


## 📕+🔮Human-Centered AI and Natural Language Processing
💡[Text Games](https://www.textgames.org/learn-more/) (or, Interactive Fiction, or [Text-based Virtual Environments](assets/blog/groupmeeting.pdf) are interactive virtual worlds that users observe and act upon using words instead of pixels.

- <span style="color: #9C27B0; font-weight:bold;">[Conference]</span> 
-- ``Computer Science and Information Technology`` **"Design and Optimization of Reinforcement Learning-Based Agents in Text-Based Games"**  
<span style="color:darkblue">**Haonan Wang**</span>, Mingjia Zhao，Junfeng Sun,Wei Liu.\
International Journal of Computer Science and Information Technology, 2025.[[pdf]](https://wepub.org/index.php/IJCSIT/article/view/5152),

  
 - <span style="color:green; font-weight:bold;">[Journal]</span>
-- ``Computer Science and AI`` **"Research on the Integration of Embodied Intelligence and Reinforcement Learning in Textual Domains"**  
<span style="color:darkblue">**Haonan Wang**</span>,Junfeng Sun,Mingjia Zhao, Wei Liu.\
Journal of Computer Science and Artificial Intelligence, 2025. [[pdf]](),

  
## 📙+⏳Machine learning and Reinforcement learning

- <span style="color:green; font-weight:bold;">[Journal]</span> 
-- ``Plos one`` **"Unsupervised Feature Selection Algorithm Based on L2,p-norm Feature Reconstruction"**  
  Wei Liu, Miao Zhong, Guangwei Liu,<span style="color:darkblue">**Haonan Wang**</span> , Ning Qian.\
Plos one, 2025. 

- <span style="color:green; font-weight:bold;">[Journal]</span> 
-- ``Chinese Journal of Image and Graphics(Chinese language)`` **"Detail-enhanced medical image segmentation focusing on global and intermediate features"**  
  Ruiyang Wang,<span style="color:darkblue">**Haonan Wang**</span>,Junfeng Sun,Mingjia Zhao,Meng Liu.\
Advances in Artificial Intelligence and Machine Learning, 2025.  <details style="display:inline;">
  <summary style="display:inline; cursor:pointer; color:blue; text-decoration:underline;">Abstract</summary>
  Objective Medical image segmentation is a crucial and challenging task in the field of not only medical imaging but also modern medicine. Segmentation techniques can be used to precisely locate and measure tumors, blood vessels, and other structures, which facilitate the early diagnosis of the disease and the evaluation of treatment outcomes. In addition, accurate and reliable medical image segmentation can be utilized to monitor disease progression, assist physicians in formulating long-term treatment plans, lay a solid foundation for clinical diagnosis and pathological research, and provide valuable data support. Feature fusion in medical image segmentation can comprehensively capture detailed and global information by combining multi-level, multi-scale, and multimodal features, which improves segmentation accuracy and robustness. This method not only enhances the capability of automated medical image processing and reduces dependence on large amounts of annotated data but also increases the accuracy of clinical decisions. This approach helps doctors make highly reliable judgments in diagnosis and treatment, which promote the development of medical automation. In medical image segmentation, upsampling strategies can effectively restore high-resolution features and detailed information, which enhances the capability of the segmentation model to recognize small structures and boundaries. By adopting appropriate upsampling methods, the spatial information of the original image can be preserved and recovered, which improves the precision of segmentation. This enhancement not only aids in the precise localization of lesion areas and the extraction of biological features but also holds significant importance for clinical diagnosis and treatment decision making. The advancement of artificial intelligence has facilitated the wide application of deep learning techniques. However, these deep learning methods often employ top-down or bottom-up approaches for feature fusion, which can result in the neglect or loss of intermediate layer feature information. Moreover, existing methods still encounter issues with imprecise segmentation boundaries of lesion areas, which leads to the omission of critical information when dealing with fine structures and complex background information. To address these concerns, this study proposes a Detail-Enhanced Medical Image Segmentation Network Focusing on Global and Intermediate Features (DEMS-GIF). Method First, to address the shortcomings of existing feature fusion methods in capturing complex structures and integrating intermediate features, this study proposes a Transformer-based bridge feature fusion (TBBFF) module. Compared with other feature fusion modules, the TBBFF module focuses more on intermediate feature information and leverages the capability of the Transformer to capture long-range dependencies between different regions. These features enable the network to better understand the overall structure and contextual information of the image, which further enhances the segmentation performance and robustness of the model. Second, to address the issues of excessive smoothness in generated images and the lack of precise boundary segmentation in the areas of lesion using existing methods, this study proposes an expanded and scale-region-enhanced upsampling strategy under reverse attention (ESRU strategy). By incorporating a reverse attention mechanism and combining erosion and dilation operations, the model can better capture boundary and detail information in the target regions of medical images, which enhances the integrity and continuity of the segmented regions. This enhancement, in turn, improves the accuracy and stability of segmentation. In conclusion, the DEMS-GIF model, which integrating the TBBFF module and the ESRU strategy, effectively extracts image details and global information. Thus, it ensures the integrity of the segmented regions and further enhances segmentation accuracy. Result We evaluated the superiority of the DEMS-GIF model by comparing it with recent and classic methods through applying them on three different datasets: CVC-ClinicDB, DDTI, and Kvasir-SEG. The experimental results demonstrate that, on the CVC-ClinicDB dataset, the DEMS-GIF model achieved mIoU and Dice scores of 94.74% and 94.82%, respectively. Compared with recently proposed segmentation methods, the mIoU achieved by DEMS-GIF outperformed those of MSUNet, MBSNet, and SCSONet by 3.98%, 4.42%, and 20.13%, respectively. With an increase in training iterations, the train loss of DEMS-GIF decreased significantly and was notably lower than those of ResUNet++ and SCSONet. On the DDTI dataset, the DEMS-GIF model achieved a precision of 85.52% and an mIoU of 84.56%. Compared with traditional network models, DEMS-GIF showed the most significant differences with ResNet++, with precision and mIoU higher by 13.97% and 10.96%, respectively. In addition, the train loss of DEMS-GIF was noticeably lower than those of other models, with the most significant difference observed with MFSNet. On the Kvasir-SEG dataset, the DEMS-GIF model achieved mIoU and Dice scores of 87.44%. Its mIoU was 12.69% higher than that of ResUNet++, and its Dice was 6.82% higher than that of UNet, which demonstrates substantial superiority. Compared with those of other models such as MBSNet, DTA-UNet, and SCSONet, the mIoU of DEMS-GIF was higher by 6.77%, 3.84%, and 25.02%, respectively, which suggests the best performance. During training, the train loss of DEMS-GIF was significantly lower than those of other network models, except that of MFSNet. We also conducted ablation experiments to understand the effectiveness of each module and structure within DEMS-GIF. The ablation experiments were divided into module ablation and parameter ablation. The module ablation experiments were conducted on the CVC-ClinicDB, DDTI, and Kvasir-SEG datasets, and the parameter ablation experiments were performed on the CVC-ClinicDB dataset. Using Res2Net as the baseline network, the module ablation experiments thoroughly discussed the impact of the TBBFF module and ESRU strategy on model performance. The results demonstrated that the combination of the TBBFF module and ESRU strategy allows the network to focus more on lesion areas, which results in more accurate segmentation. Parameter ablation involved experiments on the threshold and adaptive parameters used in reweighting with erosion and dilation operations. The findings illustrated the contribution of each parameter in the DEMS-GIF model and identified the optimal parameter values. As a result, the model settings are optimized to further enhance the overall performance and reliability of the model. Conclusion In this study, we propose DEMS-GIF, which integrates the TBBFF module and the ESRU strategy. The network effectively leverages intermediate layer feature information to integrate features across different scales and levels. It also enhances the focus on boundary and detail information of lesion areas, which realizes efficient extraction and refined processing of image features. This process results in more complete and accurate segmentation regions. Experimental results show that the proposed DEMS-GIF network model outperforms other advanced segmentation methods, which demonstrates its superiority in medical image segmentation.
  </details>

- <span style="color:green; font-weight:bold;">[Journal]</span> 
-- ``Scientific Reports`` **"IM3HRL: Model-assisted Intrinsically Motivated Modular Hierarchical Reinforcement Learning"**  
Wei Liu,Jiaxiang Wang,Guangwei Liu, <span style="color:darkblue">**Haonan Wang**</span>.\
Scientific Reports, 2024. [[pdf]](https://www.researchsquare.com/article/rs-4299675/v1),



- <span style="color:green; font-weight:bold;">[Journal]</span> 
-- ``Scientific Journal`` **"Research status and future prospects of machine learning algorithm in big data analysis"**  
  <span style="color:darkblue">**Haonan Wang**</span>.\
Scientific Journal of Intelligent Systems Research,2022. [[pdf]](https://www.clausiuspress.com/article/1212.html),


- <span style="color:green; font-weight:bold;">[Journal]</span> 
-- ``Advances in AI and ML`` **"Research on geometric figure classification algorithm based on Deep Learning"**  
  Ruiyang Wang,<span style="color:darkblue">**Haonan Wang**</span>,Junfeng Sun,Mingjia Zhao,Meng Liu.\
Advances in Artificial Intelligence and Machine Learning, 2022. [[pdf]](https://arxiv.org/abs/2404.16561),

- <span style="color:green; font-weight:bold;">[Journal]</span> 
-- ``Advances in AI and ML`` **"Research on geometric figure classification algorithm based on Deep Learning"**  
  Ruiyang Wang,<span style="color:darkblue">**Haonan Wang**</span>,Junfeng Sun,Mingjia Zhao,Meng Liu.\
Advances in Artificial Intelligence and Machine Learning, 2022. [[pdf]](https://arxiv.org/abs/2404.16561),

## 📗+🔍Other Field
### 🖥Software Patents:
[P.1] <span style="color:darkblue">**Haonan Wang**</span>, Mingjia, Zhao, et al. (2022). **Artificial intelligence robot programming interactive control
system**. PRC Software Copyright Patent, Patent No. 2022SR1053901.\
[P.2] <span style="color:darkblue">**Haonan Wang**</span>, Junfeng, Sun, et al. (2022). **Image recognition processing operation platform**. PRC Software
Copyright Patent, Patent No. 2022SR1052419.\
[P.3] <span style="color:darkblue">**Haonan Wang**</span>, Chang, Liu, et al. (2022). **Artificial Intelligence Community Security Equipment Monitoring
System**. PRC Software Copyright Patent, Patent No. 2022SR1052492.\
[P.4] <span style="color:darkblue">**Haonan Wang**</span>, Meng, Liu, et al. (2022). **A network behavior analysis system based on machine
learning**. PRC Software Copyright Patent, Patent No. 2022SR1049807.\
[P.5] <span style="color:darkblue">**Haonan Wang**</span>, Chi, Li, et al. (2022). **Autonomous Driving Intelligent Dispatching Center Management
System**. PRC Software Copyright Patent, Patent No. 2022SR1052526.\
[P.6] <span style="color:darkblue">**Haonan Wang**</span>, Ruiyang, Wang, et al. (2022). **Unmanned shortest path planning system**. PRC Software
Copyright Patent, Patent No.2022SR0935020.\
[P.7] <span style="color:darkblue">**Haonan Wang**</span>, Junfeng Sun, et al. (2022). **Data operation analysis and collection system based on machine
learning**. PRC Software Copyright Patent, Patent No. 2022SR1052428.\
[P.8] Jiawei, Zhang, Pengyu, Cai, <span style="color:darkblue">**Haonan Wang**</span>, et al. (2021). **Staff check-in face recognition system**.PRC Software
Copyright. PRC Software Copyright Patent, Patent No. 2021SR0699354.

### 📊Competition Awards(Mathematical Modeling and Computer Science Design):
• 1st Place, 12th MathorCup College Mathematical Modeling Challenge 2022\
National-level award in China\
• 1st Place, Liaoning Mathematical Modeling Contest 2022\
Provincial-level award in China\
• 1st Place, 7th Shuwei Mathematical Modeling Challenge for College Students 2022\
National-level award in China\
• 1st Place, 12th MathorCup College Mathematical Modeling Challenge 2022\
National-level award in China\
• 3rd Place, Liaoning Province "Shuo Ri Cup" College Student Computer Design 2022\
Provincial-level award in China\
• 3rd Place, Northeast Three Provinces Mathematical Modeling Competition 2022\
Provincial-level award in China\
• 2nd Place, American Mathematical Contest in Modeling 2022\
International award\
• 3rd Place, 14th National Undergraduate Computer Design Competition 2021\
National-level award in China\
• 3rd Place, 11th Mathor Cup University Mathematical Modeling Challenge 2021\
National-level award in China\
• 2nd Place, National College Students "Hua Shu Cup" Mathematical Modeling 2021\
National-level award in China\
• 1st Place, Liaoning Province "Shuo Ri Cup" College Student Computer Design 2021\
Provincial-level award in China,\
• 1st Place, Liaoning AgricuLNTUral Economic Modeling Competition 2021\
Provincial-level award in China\
• 1st Place, Outstanding Scholarship of the Faculty of Science, LNTU 2021\
School-level award in China\
• 1st Place, Career Planning Competition of the Faculty of Science, LNTU 2021\
School-level award in China\
• Academic Achievement Award of the School of Science, LNTU 2021\
School-level award in China\
• 2nd Place, Liaoning Mathematical Modeling Contest 2021\
Provincial-level award for China














