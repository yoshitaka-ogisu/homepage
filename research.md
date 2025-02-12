---
title: Research
layout: landing
description: Publications and Projects
image: assets/images/pic07.jpg
nav-menu: true
---

<!-- Main -->
<div id="main">


<section id="two">
	<div class="inner">
		<header class="major">
			<h2>Preprints</h2>
		</header>
		<ul class="alt">
			{% for pub in site.data.preprints %}
			<li>{{ pub.authors | join: ', ' }} ({{ pub.year }}) ''{{ pub.title }},'' <a href="{{ pub.link }}">{{ pub.pub_by }}</a>.</li>
			{% endfor %}
		</ul>
	</div>
</section>

<!-- Three -->
<section id="three" class="spotlights">
	<section>
		<a href="profile.html" class="image">
			<img src="{{ '/assets/images/pic08.jpg' | relative_url }}" alt="Work in Progress" />
		</a>
		<div class="content">
			<div class="inner">
				<header class="major">
					<h3>Work in progress</h3>
				</header>
				<div>
					<ul class="alt">
						{% for pub in site.data.working %}
							<li>{{ pub.title }} (related with {{ pub.field | join: ', ' }}).</li>
						{% endfor %}
					</ul>
				</div>
			</div>
		</div>
	</section>
</section>


<section id="four" class="spotlights">
	<section>
		<div class="image">
            <div style="height: 100%; background-color: #f6f6f6; display: flex; justify-content: center; align-items: center; position: relative; overflow: hidden;">
                <svg width="100%" height="100%" style="position: absolute; top: 0; left: 0; opacity: 0.15;">
                    <defs>
                        <linearGradient id="nodeGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                            <stop offset="0%" style="stop-color:#242943;stop-opacity:1" />
                            <stop offset="100%" style="stop-color:#45558d;stop-opacity:1" />
                        </linearGradient>
                    </defs>
                    <!-- 中心の大きなノード -->
                    <circle cx="50%" cy="50%" r="5" fill="url(#nodeGradient)"/>
                    
                    <!-- 周囲のノードとエッジ -->
                    <circle cx="30%" cy="30%" r="3" fill="url(#nodeGradient)"/>
                    <line x1="50%" y1="50%" x2="30%" y2="30%" stroke="#242943" stroke-width="0.5"/>
                    
                    <circle cx="70%" cy="30%" r="3" fill="url(#nodeGradient)"/>
                    <line x1="50%" y1="50%" x2="70%" y2="30%" stroke="#242943" stroke-width="0.5"/>
                    
                    <circle cx="30%" cy="70%" r="3" fill="url(#nodeGradient)"/>
                    <line x1="50%" y1="50%" x2="30%" y2="70%" stroke="#242943" stroke-width="0.5"/>
                    
                    <circle cx="70%" cy="70%" r="3" fill="url(#nodeGradient)"/>
                    <line x1="50%" y1="50%" x2="70%" y2="70%" stroke="#242943" stroke-width="0.5"/>
                    
                    <!-- 追加のノードとエッジ -->
                    <circle cx="20%" cy="50%" r="2" fill="url(#nodeGradient)"/>
                    <line x1="30%" y1="30%" x2="20%" y2="50%" stroke="#242943" stroke-width="0.5"/>
                    
                    <circle cx="80%" cy="50%" r="2" fill="url(#nodeGradient)"/>
                    <line x1="70%" y1="30%" x2="80%" y2="50%" stroke="#242943" stroke-width="0.5"/>
                    
                    <circle cx="50%" cy="20%" r="2" fill="url(#nodeGradient)"/>
                    <line x1="30%" y1="30%" x2="50%" y2="20%" stroke="#242943" stroke-width="0.5"/>
                    
                    <circle cx="50%" cy="80%" r="2" fill="url(#nodeGradient)"/>
                    <line x1="30%" y1="70%" x2="50%" y2="80%" stroke="#242943" stroke-width="0.5"/>
                </svg>
                <h1 style="color: #242943; font-size: 2em; position: relative; z-index: 1; text-transform: uppercase;">Publications</h1>
            </div>
        </div>
		<div class="content">
			<div class="inner">
				<ul class="alt">
					{% for pub in site.data.publications %}
						<li>{{ pub.authors | join: ', ' }} ({{ pub.year }}) ''{{ pub.title }},'' <em><a href="{{ pub.link }}">{{ pub.journal }}</a></em>, {{pub.volume}}.</li>
					{% endfor %}
				</ul>
			</div>
		</div>
	</section>
	<section>
		<a href="generic.html" class="image">
			<img src="{% link assets/images/pic09.jpg %}" alt="" data-position="top center" />
		</a>
		<div class="content">
			<div class="inner">
				<header class="major">
					<h3>Rhoncus magna</h3>
				</header>
				<p>Nullam et orci eu lorem consequat tincidunt vivamus et sagittis magna sed nunc rhoncus condimentum sem. In efficitur ligula tate urna. Maecenas massa sed magna lacinia magna pellentesque lorem ipsum dolor. Nullam et orci eu lorem consequat tincidunt. Vivamus et sagittis tempus.</p>
				<ul class="actions">
					<li><a href="generic.html" class="button">Learn more</a></li>
				</ul>
			</div>
		</div>
	</section>
	<section>
		<a href="generic.html" class="image">
			<img src="{% link assets/images/pic10.jpg %}" alt="" data-position="25% 25%" />
		</a>
		<div class="content">
			<div class="inner">
				<header class="major">
					<h3>Sed nunc ligula</h3>
				</header>
				<p>Nullam et orci eu lorem consequat tincidunt vivamus et sagittis magna sed nunc rhoncus condimentum sem. In efficitur ligula tate urna. Maecenas massa sed magna lacinia magna pellentesque lorem ipsum dolor. Nullam et orci eu lorem consequat tincidunt. Vivamus et sagittis tempus.</p>
				<ul class="actions">
					<li><a href="generic.html" class="button">Learn more</a></li>
				</ul>
			</div>
		</div>
	</section>
</section>

</div>
