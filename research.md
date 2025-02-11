---
title: Research
layout: landing
description: Publications and Projects
image: assets/images/pic07.jpg
nav-menu: true
---

<!-- Main -->
<div id="main">

<!-- One -->
<section id="one">
	<div class="inner">
		<header class="major">
			<h2>Publications</h2>
		</header>
			{% for pub in site.data.publications %}
		<div class="publication-entry">
			{{ pub.authors | join: ', ' }} ({{ pub.year }}) ''{{ pub.title }},'' <em><a href="{{ pub.link }}">{{ pub.journal }}</a></em>, {{pub.volume}}.
		</div>
		{% endfor %}
	</div>
</section>

<section id="two">
	<div class="inner">
		<header class="major">
			<h2>Publications</h2>
		</header>
			{% for pub in site.data.preprints %}
		<div class="publication-entry">
			{{ pub.authors | join: ', ' }} ({{ pub.year }}) ''{{ pub.title }},'' <a href="{{ pub.link }}">{{ pub.pub_by }}</a>.
		</div>
		{% endfor %}
	</div>
</section>

<!-- Three -->
<section id="three" class="inner">
	<section>
		<a href="profile.html" class="image">
			<img src="{% assets/images/pic8.jpg %}" alt="" data-position="center center" />
		</a>
		<div class="content">
			<div class="inner">
				<header class="major">
					<h3>Work in progress</h3>
				</header>
				{% for pub in site.data.working %}
				<div class="publication-entry">
					{{ pub.title }} (related with {{ pub.field | join: ', ' }}).
				</div>
				{% endfor %}
			</div>
		</div>
	</section>
</section>


</div>
