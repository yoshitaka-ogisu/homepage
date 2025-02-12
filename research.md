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
            <img src="{{ 'assets/images/network_communities.svg' | relative_url }}" alt="Network Visualization" style="opacity: 0.2;"/>
            <h1 style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: #242943; font-size: 2em; text-transform: uppercase; margin: 0;">Publications</h1>
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
