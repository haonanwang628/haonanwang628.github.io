# 📖 Publications 

<style>
  .pub-filter-btn {
    background: none;
    border: none;
    color: #2b6cb0;
    padding: 0;
    font: inherit;
    cursor: pointer;
    text-decoration: underline;
  }
  .pub-filter-btn:hover {
    color: #1a365d;
  }
  
  /* 1. 文章标题设为纯文本黑色 */
  .pub-title {
    color: #111827;
    font-size: 15px;
  }

  /* 2. 底部元信息栏 */
  .pub-meta {
    margin-left: 16px;
    margin-top: 4px;
    font-size: 14px;
    color: #6b7280; /* 斜杠 / 颜色 */
  }
  
  /* 会议/期刊名称：黑色 + 加粗 */
  .venue-title {
    font-weight: 800;
    color: #1d4ed8; /* 经典的皇家深蓝/宝蓝 */
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    letter-spacing: 0.2px; /* 微调字符间距，更有出版物质感 */
  
  /* 资源链接（Paper/Code/Slides等）：蓝色 */
  .pub-meta a {
    color: #2563eb;
    text-decoration: none;
  }
  .pub-meta a:hover {
    text-decoration: underline;
  }
</style>

<!-- 1. 顶部切换菜单 -->
<div style="margin-bottom: 20px; font-size: 16px;">
  <button type="button" class="pub-filter-btn" onclick="showSection('date')" id="btn-date" style="font-weight: bold;">by date:all</button> / 
  <button type="button" class="pub-filter-btn" onclick="showSection('topic')" id="btn-topic">by topic</button> / 
  <button type="button" class="pub-filter-btn" onclick="showSection('featured')" id="btn-featured">featured</button>
</div>

<!-- 2. 按 Date 分组视图 -->
<div id="section-date" class="pub-section">
  {% assign years = site.data.publications | map: "year" | uniq | sort | reverse %}
  {% for y in years %}
    <h2 style="margin-top: 25px; border-bottom: 1px solid #eee; padding-bottom: 5px;">{{ y }}</h2>
    {% assign year_papers = site.data.publications | where: "year", y %}
    {% for paper in year_papers %}
      <div style="margin-bottom: 20px;">
        <div class="pub-title">
          <strong>{{ paper.title }}</strong>
        </div>
        
        <div style="margin-top: 4px;">
          &nbsp;&nbsp;&nbsp;&nbsp;{{ paper.authors }}
        </div>

        <div class="pub-meta">
          {% assign links = "" | split: "," %}
          
          {% if paper.venue %}
            {% capture v %}<span class="venue-title">{{ paper.venue }}</span>{% endcapture %}
            {% assign links = links | push: v %}
          {% endif %}
          
          {% if paper.paper_url %}
            {% capture p %}<a href="{{ paper.paper_url }}" target="_blank">Paper</a>{% endcapture %}
            {% assign links = links | push: p %}
          {% endif %}

          {% if paper.code_url %}
            {% capture c %}<a href="{{ paper.code_url }}" target="_blank">Code</a>{% endcapture %}
            {% assign links = links | push: c %}
          {% endif %}

          <!-- 👇 1. 支持 Slides 链接 -->
          {% if paper.slides_url %}
            {% capture s %}<a href="{{ paper.slides_url }}" target="_blank">Slides</a>{% endcapture %}
            {% assign links = links | push: s %}
          {% endif %}

          <!-- 👇 2. 支持 Poster Recording / Video 链接 -->
          {% assign rec_url = paper['poster-recording_url'] | default: paper.video_url %}
          {% if rec_url %}
            {% capture rec %}<a href="{{ rec_url }}" target="_blank">Video</a>{% endcapture %}
            {% assign links = links | push: rec %}
          {% endif %}

          {% if paper.project_url %}
            {% capture b %}<a href="{{ paper.project_url }}" target="_blank">Project</a>{% endcapture %}
            {% assign links = links | push: b %}
          {% endif %}

          {{ links | join: " / " }}
        </div>
      </div>
    {% endfor %}
  {% endfor %}
</div>

<!-- 3. 按 Topic 分组视图 -->
<div id="section-topic" class="pub-section" style="display: none;">
  {% assign topics = "Legal AI,Large Language Model Technologies,Machine Learning" | split: "," %}
  {% for t in topics %}
    {% assign topic_papers = site.data.publications | where: "topic", t %}
    {% if topic_papers.size > 0 %}
      <h2 style="margin-top: 25px; border-bottom: 1px solid #eee; padding-bottom: 5px;">{{ t }}</h2>
      {% for paper in topic_papers %}
        <div style="margin-bottom: 20px;">
          <div class="pub-title">
            <strong>{{ paper.title }}</strong>
          </div>
          <div style="margin-top: 4px;">
            &nbsp;&nbsp;&nbsp;&nbsp;{{ paper.authors }}
          </div>
          <div class="pub-meta">
            {% assign links = "" | split: "," %}
            {% if paper.venue %}{% capture v %}<span class="venue-title">{{ paper.venue }}</span>{% endcapture %}{% assign links = links | push: v %}{% endif %}
            {% if paper.paper_url %}{% capture p %}<a href="{{ paper.paper_url }}" target="_blank">Paper</a>{% endcapture %}{% assign links = links | push: p %}{% endif %}
            {% if paper.code_url %}{% capture c %}<a href="{{ paper.code_url }}" target="_blank">Code</a>{% endcapture %}{% assign links = links | push: c %}{% endif %}
            {% if paper.slides_url %}{% capture s %}<a href="{{ paper.slides_url }}" target="_blank">Slides</a>{% endcapture %}{% assign links = links | push: s %}{% endif %}
            {% assign rec_url = paper['poster-recording_url'] | default: paper.video_url %}
            {% if rec_url %}{% capture rec %}<a href="{{ rec_url }}" target="_blank">Video</a>{% endcapture %}{% assign links = links | push: rec %}{% endif %}
            {% if paper.project_url %}{% capture b %}<a href="{{ paper.project_url }}" target="_blank">Project</a>{% endcapture %}{% assign links = links | push: b %}{% endif %}
            {{ links | join: " / " }}
          </div>
        </div>
      {% endfor %}
    {% endif %}
  {% endfor %}
</div>

<!-- 4. Featured 精选视图 -->
<div id="section-featured" class="pub-section" style="display: none;">
  <h2 style="margin-top: 25px; border-bottom: 1px solid #eee; padding-bottom: 5px;">Featured Publications</h2>
  {% assign featured_papers = site.data.publications | where: "featured", true %}
  {% for paper in featured_papers %}
    <div style="margin-bottom: 20px;">
      <div class="pub-title">
        <strong>{{ paper.title }}</strong>
      </div>
      <div style="margin-top: 4px;">
        &nbsp;&nbsp;&nbsp;&nbsp;{{ paper.authors }}
      </div>
      <div class="pub-meta">
        {% assign links = "" | split: "," %}
        {% if paper.venue %}{% capture v %}<span class="venue-title">{{ paper.venue }}</span>{% endcapture %}{% assign links = links | push: v %}{% endif %}
        {% if paper.paper_url %}{% capture p %}<a href="{{ paper.paper_url }}" target="_blank">Paper</a>{% endcapture %}{% assign links = links | push: p %}{% endif %}
        {% if paper.code_url %}{% capture c %}<a href="{{ paper.code_url }}" target="_blank">Code</a>{% endcapture %}{% assign links = links | push: c %}{% endif %}
        {% if paper.slides_url %}{% capture s %}<a href="{{ paper.slides_url }}" target="_blank">Slides</a>{% endcapture %}{% assign links = links | push: s %}{% endif %}
        {% assign rec_url = paper['poster-recording_url'] | default: paper.video_url %}
        {% if rec_url %}{% capture rec %}<a href="{{ rec_url }}" target="_blank">Video</a>{% endcapture %}{% assign links = links | push: rec %}{% endif %}
        {% if paper.project_url %}{% capture b %}<a href="{{ paper.project_url }}" target="_blank">Project</a>{% endcapture %}{% assign links = links | push: b %}{% endif %}
        {{ links | join: " / " }}
      </div>
    </div>
  {% endfor %}
</div>

<!-- 5. 切换脚本 -->
<script>
function showSection(type) {
  const sections = document.querySelectorAll('.pub-section');
  sections.forEach(sec => sec.style.display = 'none');
  
  document.getElementById('section-' + type).style.display = 'block';

  document.getElementById('btn-date').style.fontWeight = type === 'date' ? 'bold' : 'normal';
  document.getElementById('btn-topic').style.fontWeight = type === 'topic' ? 'bold' : 'normal';
  document.getElementById('btn-featured').style.fontWeight = type === 'featured' ? 'bold' : 'normal';
}
</script>



# 🖥 Software and Competition Awards
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














