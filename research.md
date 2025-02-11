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
			{{ pub.authors | join: ', ' }} ({{ pub.year }}), ``{{ pub.title }},'' <em><a href="{{ pub.link }}">{{ pub.journal }}</a></em>, {{pub.volume}}.
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
		<div>
			<h5>
			{{ pub.authors | join: ', ' }} ({{ pub.year }}), ``{{ pub.title }},'' <a href="{{ pub.link }}">{{ pub.pub_by }}</a>.
			</h5>
		</div>
		{% endfor %}
	</div>
</section>

<!-- Two -->
<section id="two" class="inner">
	<section>
		<a href="profile.html" class="image">
			<img src="{% link assets/images/pic08.jpg %}" alt="" data-position="center center" />
		</a>
		<div class="content">
			<div class="inner">
				<header class="major">
					<h3>Work in progress</h3>
				</header>
				<p></p>
				<ul class="actions">
					<li><a href="profile.html" class="button">Learn more</a></li>
				</ul>
			</div>
		</div>
	</section>
</section>




</div>
