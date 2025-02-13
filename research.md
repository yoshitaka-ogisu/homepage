---
title: Research
layout: landing
description: Publications and Projects
image: assets/images/network_communities_seven.svg
nav-menu: true
---

<!-- Main -->
<div id="main">

<section id="one">
	<br>
</section>

<section id="two" class="spotlights">
	<section class="scroll-fade">
		<div class="image">
            <img src="{{ 'assets/images/network_communities.svg' | relative_url }}" alt="Publications" style="opacity: 0.7;" data-position="center center" />
            <h1 style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color:#ffffff; font-size: 2em; text-transform: uppercase; margin: 0;">Publications</h1>
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
	<section class="scroll-fade">
		<div class="image">
            <img src="{{ 'assets/images/network_preprints.svg' | relative_url }}" alt="Preprints" style="opacity: 0.6;" data-position="top center" />
            <h1 style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color:#ffffff; font-size: 2em; text-transform: uppercase; margin: 0;">Preprints</h1>
        </div>
		<div class="content">
			<div class="inner">
				<ul class="alt">
					{% for pub in site.data.preprints %}
					<li>{{ pub.authors | join: ', ' }} ({{ pub.year }}) ''{{ pub.title }},'' <a href="{{ pub.link }}">{{ pub.pub_by }}</a>.</li>
					{% endfor %}
				</ul>
			</div>
		</div>
	</section>
	<section class="scroll-fade">
		<div class="image">
            <img src="{{ 'assets/images/network_wip.svg' | relative_url }}" alt="Work in progress" style="opacity: 0.5;" data-position="center center" />
            <h1 style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color:#ffffff; font-size: 2em; text-transform: uppercase; margin: 0;">Work in progress</h1>
        </div>
		<div class="content">
			<div class="inner">
				<ul class="alt">
					{% for pub in site.data.working %}
						<li>{{ pub.title }} (related with {{ pub.field | join: ', ' }}).</li>
					{% endfor %}
				</ul>
			</div>
		</div>
	</section>
</section>

<section>
	<div class="inner" align="center">
		<ul class="actions">
			<li><a href="index.html" class="button">Home</a></li>
			<li><a href="#banner" class="button special scroll">Page top</a></li>
		</ul>
	</div>
</section>

</div>
