---
layout: page
title: 入門マクロ経済学
description: 甲南大学/経済学部
image: 
nav-menu: false
show_tile: false
banner_style: style1
---

<!-- Main -->
<div id="main" class="alt">

<!-- One -->
<section id="one">
	<div class="inner">

<!-- Content -->


<h2>概要</h2>
<blockquote>
マクロ経済学の基礎を学びます。「マクロ経済学」とは、一国の経済を俯瞰的かつ全体的に捉え、その仕組みを明らかにする経済学の基礎的な分野です。マクロ経済学の主な課題は、一国の経済活動の規模やその変化が、どのような要因によって、いかにして決定されるのかを分析して、私たちの生活や人生に大きな影響を与えうる景気循環や経済成長などが生じる原因と仕組みを明らかにすることです。本授業科目では、そのために必要となる基礎的な諸概念とそれらの間の相互関係について学びます。（シラバスより引用）
</blockquote>

<hr class="major" />

<div class="table-wrapper">
	<table>
		<thead>
			<tr>
				<th>コンテンツ</th>
				<th>アップデート日</th>
				<th>ダウンロードリンク</th>
			</tr>
		</thead>
		<tbody>
			<tr>
				<td>入門マクロ経済学 ハンドアウト</td>
				<td>2025/2/15</td>
				<td><a href="{{ site.baseurl }}/assets/pdf/teaching/introductory_macro_handout.pdf" class="button icon fa-file-pdf-o">file</a></td>
			</tr>
		</tbody>
	</table>
</div>

<hr class="major" />

<div class="row">
	<div class="12u$ 12u$(small)">
		<h3>講義における3つのキーポイント</h3>
	</div>
	
	<div class="4u 12u$(small)">
		<h3>GDP（国内総生産）</h3>
		<p>マクロ経済の動向を捉えるための最も基本的な概念です。GDPには名目GDPと実質GDPが出てきますが、これらの違いをきっちり整理した上で、「実用上の分析の多くで実質GDPが用いられているのがなぜか」という点を考えることが重要です。また、国民経済計算（SNA）で計算されたGDPにおいては、基本的に<b>三面等価の原則</b>が成立する、という事実をおさえましょう。</p>
	</div>
	<div class="4u 12u$(small)">
		<h3>有効需要の原理</h3>
		<p>後半のケインジアンモデルにおいて扱う概念です。本講義では、「総需要が総供給に一致する」というルールのことを指します。なぜそう考えるのか（仮定するのか）？という点を、財市場、資産市場の両面から解釈できるようになることが望ましいでしょう。講義では予期せぬ在庫投資の取り扱い方を説明した後に、経済学でよく用いられる<b>均衡</b>の概念とからめて説明を行います。</p>
	</div>
	<div class="4u$ 12u$(medium)">
		<h3>乗数効果</h3>
		<p>1億円の追加需要が発生した時に、その需要の増加がトリガーとなり、消費需要を連鎖的に増加させていきます。したがって、最終的な需要の増加量は最初に発生した1億円を超えることになります。これが、乗数効果の直観的なオハナシです。講義では、図を用いた解説を交えて、メカニズムをもう少し詳しく説明します。1単位の（限界的な）需要増加がどれほどの均衡需要の増加をもたらすかを表す、”<b>乗数</b>”を理解するところが目標地点です。</p>
	</div>
</div>

<hr class="major" />


<div class="row">
	<!--質問-->
	<div class="6u 12u$(small)">
		<header>
			<h3>質問フォーム</h3>
		</header>
		<form method="post" action="https://YoshitakaOgisu.pythonanywhere.com/submit_reaction"> 
			<!-- 講義識別子 -->
			<input type="hidden" name="course_id" value="intro_macro">
			<!--コンテンツ識別子-->
			<input type="hidden" name="content_type" value="qa">
			<div class="8u 12u$(small)">
				<header>
					<h5>名前（任意）</h5>
				</header>
				<input type="text" name="student_name" id="student_name" placeholder="名無しさん"/>
			</div>
			<br>
			<!-- 質問内容 -->
			<textarea name="intromacro_question" id="intromacro_question" 
					placeholder="質問を入力してください" rows="12" required></textarea>
			<br>
			<div class="12u$" align="center">
				<ul class="actions">
					<li><input type="submit" value="質問送信" class="special" /></li>
					<li><input type="reset" value="リセット" /></li>
				</ul>
			</div>
		</form>
	</div>
	<!--RP-->
	<div class="6u$ 12u$(small)">
		<header>
			<h3>リアクションペーパー</h3>
		</header>
		<p>リアクションペーパーの提出には送信用パスワードが必要です。</p>
		<form method="post" action="https://YoshitakaOgisu.pythonanywhere.com/submit_reaction"> 
			<!-- 講義識別子 -->
			<input type="hidden" name="course_id" value="intro_macro">
			<!--コンテンツ識別子-->
			<input type="hidden" name="content_type" value="rp">
			<div class="row">
				<!-- 学生情報（任意） -->
				<div class="6u 12u$(small)">
					<header>
						<h5>学籍番号</h5>
					</header>
					<input type="text" name="student_id" id="student_id" placeholder="学籍番号（必須）" required />
				</div>
				<div class="6u$ 12u$(small)">
					<header>
						<h5>名前</h5>
					</header>
					<input type="text" name="student_name" id="student_name" placeholder="名前（必須）" required />
				</div>
			</div>
			<br>
			<h5>講義回と理解度の選択（必須）</h5>
			<div class="row">
				<div class="4u 12u$(small)">
					<!-- 講義回ボタン -->
					<div class="select-wrapper">
						<select name="n_of_lecture" id="n_of_lecture" required>
							<option value="">- 講義実施回 -</option>
							<option value="1">1</option>
							<option value="2">2</option>
							<option value="3">3</option>
							<option value="4">4</option>
							<option value="5">5</option>
							<option value="6">6</option>
							<option value="7">7</option>
							<option value="8">8</option>
							<option value="9">9</option>
							<option value="10">10</option>
							<option value="11">11</option>
							<option value="12">12</option>
							<option value="13">13</option>
							<option value="14">14</option>
							<option value="15">15</option>
						</select>
					</div>
				</div>
				<div class="8u$ 12u$(small)">
					<!-- 理解度ボタン -->
					<div class="select-wrapper">
						<select name="satisfaction" id="satisfaction" required>
							<option value="">- 講義の理解度 -</option>
							<option value="1">1. 問題なく理解できた。</option>
							<option value="2">2. 一部を除いて、概ね理解できた。</option>
							<option value="3">3. 理解できない部分が多いが、一部理解できた。</option>
							<option value="4">4. 理解できなかった。</option>
						</select>
					</div>
				</div>
			</div>
			<br>		
			<!-- リアクションペーパーの内容 -->
			<div class="12u$ 12u$">
				<h5>コメント（任意）</h5>
				<textarea name="reaction_content" id="reaction_content" 
						placeholder="コメントや質問があれば入力してください" rows="6"></textarea>
			</div>
			<br>
			<!-- 送信用パスワード確認用 -->
			<div class="12$ 12u$">
				<input type="password" name="lecture_password" id="lecture_password" placeholder="送信パスワード" required />
			</div>
			<br>
			<div class="12u$" align="center">
				<ul class="actions">
					<li><input type="submit" value="RP送信" class="special" /></li>
					<li><input type="reset" value="リセット" /></li>
				</ul>
			</div>
		</form>
	</div>
</div>

<hr>

<section>
  <div class="inner" align="center">
	<ul class="actions">
	  <li><a href="{{page.baseurl}}/03-teaching.html" class="button">Go back Teaching</a></li>
	</ul>
  </div>
</section>

<section>
  <div class="inner" align="center">
	<ul class="actions">
	  <li><a href="index.html" class="button">Home</a></li>
	  <li><a href="#banner" class="button special scroll">Page top</a></li>
	</ul>
  </div>
</section>

<!--End Contents-->
	</div>
</section>

</div>
