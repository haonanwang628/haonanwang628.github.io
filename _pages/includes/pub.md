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
  
  
  .pub-title {
    color: #111827;
    font-size: 15px;
  }

  
  .pub-meta {
    margin-left: 16px;
    margin-top: 4px;
    font-size: 14px;
    color: #6b7280; 
  }
  
  
  .venue-title {
    font-weight: 800;
    color: #1d4ed8;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    letter-spacing: 0.2px; 
  }
  
  
  .pub-meta a {
    color: #2563eb;
    text-decoration: none;
  }
  .pub-meta a: hover {
    text-decoration: underline;
  }
  .pub-toolbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  font-size: 16px;
}

.scholar-citations {
  font-size: 14px;
  color: #6b7280;
  white-space: nowrap;
  text-align: right;
}

.scholar-citations a {
  color: #2563eb;
  text-decoration: none;
  font-weight: 600;
}

.scholar-citations a:hover {
  text-decoration: underline;
}

.scholar-citations strong {
  color: #374151;
}
</style>

<div class="pub-toolbar">

  <div>
    <button type="button"
            class="pub-filter-btn"
            onclick="showSection('date')"
            id="btn-date"
            style="font-weight: bold;">by date:all</button> / 

    <button type="button"
            class="pub-filter-btn"
            onclick="showSection('topic')"
            id="btn-topic">by topic</button> / 

    <button type="button"
            class="pub-filter-btn"
            onclick="showSection('featured')"
            id="btn-featured">featured</button>
  </div>

  <div class="scholar-citations">
    <a href="https://scholar.google.com/citations?user=DBxarZYAAAAJ&hl=en"
       target="_blank">
      🌟Google Scholar
    </a>
    · [<strong>{{ site.data.scholar.citations }}</strong>] citations 🎉
  </div>

</div>


<!-- 2.  Date  -->
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

<!-- 3. Topic  -->
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

<!-- 4. Featured -->
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

<!-- 5.  -->
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


















