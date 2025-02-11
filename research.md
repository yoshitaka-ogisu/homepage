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
		<ul class="alt">
			{% for pub in site.data.publications %}
			<li>{{ pub.authors | join: ', ' }} ({{ pub.year }}) ''{{ pub.title }},'' <em><a href="{{ pub.link }}">{{ pub.journal }}</a></em>, {{pub.volume}}.</li>
			{% endfor %}
		</ul>
	</div>
</section>

<section id="two">
	<div class="inner">
		<header class="major">
			<h2>Publications</h2>
		</header>
		<ul>
			{% for pub in site.data.preprints %}
			<li>{{ pub.authors | join: ', ' }} ({{ pub.year }}) ''{{ pub.title }},'' <a href="{{ pub.link }}">{{ pub.pub_by }}</a>.<li>
			{% endfor %}
		</ul>
	</div>
</section>

<!-- Three -->
<section id="three"　class="spotlights">
	<section>
		<a href="profile.html" class="image">
			<img src="/assets/images/pic08.jpg" alt="" data-position="center center" />
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
