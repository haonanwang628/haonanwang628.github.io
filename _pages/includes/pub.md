# 🤔 Publications 

# 😃 Publications

<!-- 1. 顶部切换按钮菜单 -->
<div style="margin-bottom: 20px; font-size: 16px;">
  <a href="javascript:void(0)" onclick="filterPapers('date')" id="btn-date" style="font-weight: bold;">by date:all</a> / 
  <a href="javascript:void(0)" onclick="filterPapers('topic')" id="btn-topic">by topic</a> / 
  <a href="javascript:void(0)" onclick="filterPapers('featured')" id="btn-featured">featured</a>
</div>

<!-- 2. 动态渲染内容的容器 -->
<div id="paper-container"></div>

<!-- 3. 数据与逻辑脚本 -->
<script>
// 将你的论文数据整理为 JSON 数组
const papers = [
  {
    title: "Position: Large Language Models are Insufficient for Complex Real-World Legal Argumentation Mining",
    authors: "<strong>Haonan Wang</strong>, Mingjia Zhao, Sungbin Park, Vitor Ribas Moura, Effat Farhana.",
    venue: "arXiv 2026",
    year: 2026,
    topic: "Legal AI",
    featured: false,
    link: "#"
  },
  {
    title: "PerspectiveCoder-LM: An LLM-based Multi-agent System...",
    authors: "<strong>Haonan Wang</strong>, Ziang Xiao, Jie Gao.",
    venue: "arXiv 2025",
    year: 2025,
    topic: "Multi-Agent",
    featured: true,
    link: "https://github.com/isle-dev/PerspectiveCoder-LM",
    abstract: "PerspectiveCoder-LM is an LLM-based multi-perspective agent system..."
  }
  // 在这里继续添加你的其他论文...
];

function filterPapers(type) {
  const container = document.getElementById('paper-container');
  container.innerHTML = '';

  if (type === 'date') {
    // 按年份分组
    const years = [...new Set(papers.map(p => p.year))].sort((a, b) => b - a);
    years.forEach(year => {
      let html = `<h2>${year}</h2>`;
      const list = papers.filter(p => p.year === year);
      html += renderList(list);
      container.innerHTML += html;
    });
  } else if (type === 'topic') {
    // 按主题分组
    const topics = [...new Set(papers.map(p => p.topic))];
    topics.forEach(topic => {
      let html = `<h2>${topic}</h2>`;
      const list = papers.filter(p => p.topic === topic);
      html += renderList(list);
      container.innerHTML += html;
    });
  } else if (type === 'featured') {
    // 精选
    const list = papers.filter(p => p.featured);
    container.innerHTML = `<h2>Featured Publications</h2>` + renderList(list);
  }
}

function renderList(list) {
  return list.map(item => `
    <div style="margin-bottom: 15px;">
      <div><a href="${item.link}"><strong>[${item.title}]</strong></a></div>
      <div>&nbsp;&nbsp;&nbsp;&nbsp;${item.authors}</div>
      ${item.abstract ? `
        <details style="margin-left: 20px;">
          <summary><strong>Abstract</strong></summary>
          <p>${item.abstract}</p>
        </details>
      ` : ''}
    </div>
  `).join('');
}

// 页面首次加载时渲染默认按日期
filterPapers('date');
</script>

## 2026

[Position:Large Language Models are Insufficient for Complex Real-World Legal Argumentation Mining]()\\
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:darkblue">**Haonan Wang**</span>, Mingjia Zhao, Sungbin Park, Vitor Ribas Moura, Effat Farhana.

## 2025

[PerspectiveCoder-LM: An LLM-based Multi-agent System for Large-scale Corpus Inductive Text Coding Analysis](https://github.com/isle-dev/PerspectiveCoder-LM) \\
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:darkblue">**Haonan Wang**</span>,Ziang Xiao,Jie Gao.

<details>
<summary>
  <strong>Abstract</strong>
   &nbsp;&nbsp;&nbsp;
  <a href="https://github.com/isle-dev/PerspectiveCoder-LM"><strong>Project</strong></a>
</summary>

<p>
PerspectiveCoder-LM is an LLM-based multi-perspective agent system for large-scale inductive coding analysis of qualitative corpora. The system simulates multiple analytical perspectives through role-based agents, enabling LLMs to collaboratively generate, review, and refine qualitative codebooks. Given an input corpus, PerspectiveCoder-LM first produces positionality statements for different role agents, then assigns coding tasks to coder agents to generate initial codes and codebooks. Reviewer agents identify agreements and disagreements across generated codebooks, while discussion and judge agents further resolve conflicts and consolidate the final coding results. This project aims to support scalable and transparent qualitative analysis by combining multi-agent collaboration, perspective-aware reasoning, and structured codebook generation. It explores how LLMs can assist researchers in inductive coding while preserving interpretability, disagreement analysis, and multi-perspective reasoning.
</p>

</details>

[From Noise to Nuance: Enriching Subjective Data Interpretation through Qualitative Analysis](https://aclanthology.org/2025.hcinlp-1.20/) \\
 Ruyuan Wan,<span style="color:darkblue">**Haonan Wang**</span>,Ting-Hao Kenneth Huang,Jie Gao.
 
[The 4th HCI + NLP Workshop at EMNLP, 2025](https://sites.google.com/view/hciandnlp/home).

<details>
<summary>
  <strong>Abstract</strong>
  &nbsp;&nbsp;&nbsp;
  <a href="https://aclanthology.org/2025.hcinlp-1.20/"><strong>Paper</strong></a>
</summary>

<p>
 Subjective data annotation (SDA) in NLP should treat annotator disagreement as a valuable source of insight rather than noise. Drawing on qualitative data analysis (QDA), we compare the two methodologies and highlight differences in human roles, workflows, and evaluation. We propose five recommendations to make SDA more interpretive and demonstrate these ideas through a reinforcement learning from human feedback (RLHF) case study, advocating for a more interdisciplinary approach to understanding subjective data.
</p>

</details>

[ByteSized32Refactored: Towards an Extensible Interactive Text Games Corpus for LLM World Modeling and Evaluation](https://arxiv.org/abs/2509.23979) \\
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:darkblue">**Haonan Wang**</span>, Junfeng Sun, Xindi Yuan, Ruoyao Wang, Ziang Xiao.

[The 5th WordPlay Workshop at EMNLP, 2025](https://wordplay-workshop.github.io/modern/#:~:text=Overview,-Date%20and%20time&text=This%20workshop%20focused%20on%20exploring,but%20not%20limited%20to%20storytelling.).

<details>
<summary>
  <strong>Abstract</strong>
  &nbsp;&nbsp;&nbsp;
   <a href="https://arxiv.org/abs/2509.23979"><strong>Paper</strong></a>
   <a href="https://github.com/isle-dev/BYTESIZED32-Refactored/"><strong>Code</strong></a>
   <a href="https://docs.google.com/presentation/d/1fkBqKv6eUosixZW7ZpW51AjUzKbA_JZajmzdo4BR7Zc/edit?slide=id.g3881c550231_0_33#slide=id.g3881c550231_0_33"><strong>Slides</strong></a>
   <a href="assets/paper/bytesized32Refactored.mp4"><strong>Poster-recording</strong></a>
</summary>

<p>
  ByteSized32Refactored presents a modular and extensible redesign of the [original ByteSized32 interactive text games corpus](https://arxiv.org/abs/2305.14879) to advance research on LLM world modeling and evaluation. By introducing a unified foundation library that abstracts common game logic into reusable base classes, the total codebase is reduced by half while enabling easier expansion to new environments. Experiments with GPT-4o and GPT-5 demonstrate that the refactored structure improves code quality and extensibility while revealing new challenges for hierarchical reasoning in LLMs. This work establishes a scalable platform for studying interactive reasoning, adaptability, and generalization in language models.
</p>

</details>

## 2024

[Unsupervised Feature Selection Algorithm Based on L2,p-norm Feature Reconstruction](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0318431)\\
&nbsp;&nbsp;&nbsp;&nbsp;Wei liu, Miao Zhong, Guangwei Liu, <span style="color:darkblue">**Haonan Wang**</span>, Qian Ning.
[**Plos one**]().

<details>
<summary>
  <strong>Abstract</strong>
  &nbsp;&nbsp;&nbsp;
   <a href="https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0318431"><strong>Paper</strong></a>
   <a href="https://github.com/haonanwang628/UnsupervisedFSA"><strong>Code</strong></a>
</summary>

<p>
  NFRFS (an unsupervised feature selection algorithm based on L2, p-norm feature reconstruction) proposes a more robust feature selection method, aiming to address the problem that traditional algorithms are sensitive to noise and outliers. The L2 p-norm is used to enhance robustness, the integrative adaptive graph learning is employed to maintain the local structure of the data, and the inner product sparse regularization is utilized to select lower-level reference features. Experimental results on 14 benchmark datasets show that NRFFS significantly matches the existing state-of-the-art methods in Bluetooth performance, demonstrating its effectiveness and practicality in high-dimensional data processing.
</p>

</details>


## 2022

[Research on geometric figure classification algorithm based on Deep Learning](https://arxiv.org/abs/2404.16561)\\
&nbsp;&nbsp;&nbsp;&nbsp;Ruiyang Wang,<span style="color:darkblue">**Haonan Wang**</span>,Junfeng Sun,Mingjia Zhao,Meng Liu.\
Advances in Artificial Intelligence and Machine Learning, 2022.

[Research status and future prospects of machine learning algorithms in big data analysis](https://www.clausiuspress.com/article/1212.html)\\
 &nbsp;&nbsp;&nbsp;&nbsp;<span style="color:darkblue">**Haonan Wang**</span>.\
Scientific Journal of Intelligent Systems Research,2021.






# 🖥 Software 
## Software Patents :
*---🙏Thanks to the software application development collaboration with all Professors and Graduate Assistants from the **SpringTeng AI** and Liaoning Technical University, Liaoning University, and Qinghua University, being funded through our collaboration with **Chinese central State-owned Shenhua Ming Group Ltd and Zijin Ming Group Ltd enterprises**.*\
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

## Competition Awards(Mathematical Modeling and Computer Science Design):
• 1st Place, 12th Mathor Cup College Mathematical Modeling Challenge 2022\
National-level award in China\
• 1st Place, Liaoning Mathematical Modeling Contest 2022\
Provincial-level award in China\
• 1st Place, 7th Shuwei Mathematical Modeling Challenge for College Students 2022\
National-level award in China\
• 1st Place, 12th Mathor Cup College Mathematical Modeling Challenge 2022\
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














