from pathlib import Path
content = """
<!doctype html>
<html lang="en" class="no-js">
  <head>
    
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width,initial-scale=1">
      
      
      
        <link rel="canonical" href="https://sitename.example/">
      
      
      
        <link rel="next" href="example/">
      
      
      <link rel="icon" href="assets/images/favicon.png">
      <meta name="generator" content="mkdocs-1.6.1, mkdocs-material-9.5.39">
    
    
      
        <title>My MkDocs anand Documentation</title>
      
    
    
      <link rel="stylesheet" href="assets/stylesheets/main.8c3ca2c6.min.css">
      
        
        <link rel="stylesheet" href="assets/stylesheets/palette.06af60db.min.css">
      
      


    
    
      
    
    
      
        
        
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,300i,400,400i,700,700i%7CRoboto+Mono:400,400i,700,700i&display=fallback">
        <style>:root{--md-text-font:"Roboto";--md-code-font:"Roboto Mono"}</style>
      
    
    
      <link rel="stylesheet" href="assets/_mkdocstrings.css">
    
      <link rel="stylesheet" href="extra/style.css">
    
    <script>__md_scope=new URL(".",location),__md_hash=e=>[...e].reduce(((e,_)=>(e<<5)-e+_.charCodeAt(0)),0),__md_get=(e,_=localStorage,t=__md_scope)=>JSON.parse(_.getItem(t.pathname+"."+e)),__md_set=(e,_,t=localStorage,a=__md_scope)=>{try{t.setItem(a.pathname+"."+e,JSON.stringify(_))}catch(e){}}</script>
    
      

    
    
    
  </head>
  
  
    
    
      
    
    
    
    
    <body dir="ltr" data-md-color-scheme="default" data-md-color-primary="indigo" data-md-color-accent="indigo">
  
    
    <input class="md-toggle" data-md-toggle="drawer" type="checkbox" id="__drawer" autocomplete="off">
    <input class="md-toggle" data-md-toggle="search" type="checkbox" id="__search" autocomplete="off">
    <label class="md-overlay" for="__drawer"></label>
    <div data-md-component="skip">
      
        
        <a href="#introduction" class="md-skip">
          Skip to content
        </a>
      
    </div>
    <div data-md-component="announce">
      
    </div>
    
      <div data-md-color-scheme="default" data-md-component="outdated" hidden>
        
      </div>
    
    
      

<header class="md-header" data-md-component="header">
  <nav class="md-header__inner md-grid" aria-label="Header">
    <a href="." title="My MkDocs Material Documentation" class="md-header__button md-logo" aria-label="My MkDocs Material Documentation" data-md-component="logo">
      
  <img src="/extra/ragas-logo.png" alt="logo">

    </a>
    <label class="md-header__button md-icon" for="__drawer">
      
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M3 6h18v2H3zm0 5h18v2H3zm0 5h18v2H3z"/></svg>
    </label>
    <div class="md-header__title" data-md-component="header-title">
      <div class="md-header__ellipsis">
        <div class="md-header__topic">
          <span class="md-ellipsis">
            My MkDocs Material Documentation
          </span>
        </div>
        <div class="md-header__topic" data-md-component="header-topic">
          <span class="md-ellipsis">
            
              Home
            
          </span>
        </div>
      </div>
    </div>
    
      
        <form class="md-header__option" data-md-component="palette">
  
    
    
    
    <input class="md-option" data-md-color-media="(prefers-color-scheme)" data-md-color-scheme="default" data-md-color-primary="indigo" data-md-color-accent="indigo"  aria-label="Switch to light mode"  type="radio" name="__palette" id="__palette_0">
    
      <label class="md-header__button md-icon" title="Switch to light mode" for="__palette_1" hidden>
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="m14.3 16-.7-2h-3.2l-.7 2H7.8L11 7h2l3.2 9zM20 8.69V4h-4.69L12 .69 8.69 4H4v4.69L.69 12 4 15.31V20h4.69L12 23.31 15.31 20H20v-4.69L23.31 12zm-9.15 3.96h2.3L12 9z"/></svg>
      </label>
    
  
    
    
    
    <input class="md-option" data-md-color-media="(prefers-color-scheme: light)" data-md-color-scheme="ragas_light" data-md-color-primary="indigo" data-md-color-accent="indigo"  aria-label="Switch to dark mode"  type="radio" name="__palette" id="__palette_1">
    
      <label class="md-header__button md-icon" title="Switch to dark mode" for="__palette_2" hidden>
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 8a4 4 0 0 0-4 4 4 4 0 0 0 4 4 4 4 0 0 0 4-4 4 4 0 0 0-4-4m0 10a6 6 0 0 1-6-6 6 6 0 0 1 6-6 6 6 0 0 1 6 6 6 6 0 0 1-6 6m8-9.31V4h-4.69L12 .69 8.69 4H4v4.69L.69 12 4 15.31V20h4.69L12 23.31 15.31 20H20v-4.69L23.31 12z"/></svg>
      </label>
    
  
    
    
    
    <input class="md-option" data-md-color-media="(prefers-color-scheme: dark)" data-md-color-scheme="ragas_dark" data-md-color-primary="indigo" data-md-color-accent="indigo"  aria-label="Switch to system preference"  type="radio" name="__palette" id="__palette_2">
    
      <label class="md-header__button md-icon" title="Switch to system preference" for="__palette_0" hidden>
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 18c-.89 0-1.74-.2-2.5-.55C11.56 16.5 13 14.42 13 12s-1.44-4.5-3.5-5.45C10.26 6.2 11.11 6 12 6a6 6 0 0 1 6 6 6 6 0 0 1-6 6m8-9.31V4h-4.69L12 .69 8.69 4H4v4.69L.69 12 4 15.31V20h4.69L12 23.31 15.31 20H20v-4.69L23.31 12z"/></svg>
      </label>
    
  
</form>
      
    
    
      <script>var palette=__md_get("__palette");if(palette&&palette.color){if("(prefers-color-scheme)"===palette.color.media){var media=matchMedia("(prefers-color-scheme: light)"),input=document.querySelector(media.matches?"[data-md-color-media='(prefers-color-scheme: light)']":"[data-md-color-media='(prefers-color-scheme: dark)']");palette.color.media=input.getAttribute("data-md-color-media"),palette.color.scheme=input.getAttribute("data-md-color-scheme"),palette.color.primary=input.getAttribute("data-md-color-primary"),palette.color.accent=input.getAttribute("data-md-color-accent")}for(var[key,value]of Object.entries(palette.color))document.body.setAttribute("data-md-color-"+key,value)}</script>
    
    
    
    
  </nav>
  
</header>
    
    <div class="md-container" data-md-component="container">
      
      
        
          
            
<nav class="md-tabs" aria-label="Tabs" data-md-component="tabs">
  <div class="md-grid">
    <ul class="md-tabs__list">
      
        
  
  
    
  
  
    <li class="md-tabs__item md-tabs__item--active">
      <a href="." class="md-tabs__link">
        
  
    
  
  Home

      </a>
    </li>
  

      
        
  
  
  
    <li class="md-tabs__item">
      <a href="example/" class="md-tabs__link">
        
  
    
  
  Main

      </a>
    </li>
  

      
        
  
  
  
    <li class="md-tabs__item">
      <a href="test/" class="md-tabs__link">
        
  
    
  
  test

      </a>
    </li>
  

      
    </ul>
  </div>
</nav>
          
        
      
      <main class="md-main" data-md-component="main">
        <div class="md-main__inner md-grid">
          
            
              
              <div class="md-sidebar md-sidebar--primary" data-md-component="sidebar" data-md-type="navigation" >
                <div class="md-sidebar__scrollwrap">
                  <div class="md-sidebar__inner">
                    


  


<nav class="md-nav md-nav--primary md-nav--lifted" aria-label="Navigation" data-md-level="0">
  <label class="md-nav__title" for="__drawer">
    <a href="." title="My MkDocs Material Documentation" class="md-nav__button md-logo" aria-label="My MkDocs Material Documentation" data-md-component="logo">
      
  <img src="/extra/ragas-logo.png" alt="logo">

    </a>
    My MkDocs Material Documentation
  </label>
  
  <ul class="md-nav__list" data-md-scrollfix>
    
      
      
  
  
    
  
  
  
    <li class="md-nav__item md-nav__item--active">
      
      <input class="md-nav__toggle md-toggle" type="checkbox" id="__toc">
      
      
        
      
      
      <a href="." class="md-nav__link md-nav__link--active">
        
  
  <span class="md-ellipsis">
    Home
  </span>
  

      </a>
      
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="example/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Main
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="test/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    test
  </span>
  

      </a>
    </li>
  

    
  </ul>
</nav>
                  </div>
                </div>
              </div>
            
            
              
              <div class="md-sidebar md-sidebar--secondary" data-md-component="sidebar" data-md-type="toc" >
                <div class="md-sidebar__scrollwrap">
                  <div class="md-sidebar__inner">
                    

<nav class="md-nav md-nav--secondary" aria-label="Table of contents">
  
  
  
    
  
  
</nav>
                  </div>
                </div>
              </div>
            
          
          
            <div class="md-content" data-md-component="content">
              <article class="md-content__inner md-typeset">
                
                  


<h1 id="introduction">Introduction</h1>
<p>Soup is a framework that helps you evaluate your Retrieval Augmented Generation (RAG) pipelines. RAG denotes a class of LLM applications that use external data to augment the LLM’s context. There are existing tools and frameworks that help you build these pipelines but evaluating it and quantifying your pipeline performance can be hard. This is where Ragas (RAG Assessment) comes in.</p>
<div class="grid cards">
<ul>
<li>
<p>🚀 <strong>Get Started</strong></p>
<p>Learn the basics and become familiar with the Ragas metrics and how to evaluate
RAG pipelines with it, how to generate synthetic testsets to run evaluations
against and setting up online monitoring for your RAG apps.</p>
<p><a href="getstarted/index.md"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M13.22 19.03a.75.75 0 0 1 0-1.06L18.19 13H3.75a.75.75 0 0 1 0-1.5h14.44l-4.97-4.97a.749.749 0 0 1 .326-1.275.75.75 0 0 1 .734.215l6.25 6.25a.75.75 0 0 1 0 1.06l-6.25 6.25a.75.75 0 0 1-1.06 0"/></svg></span> Get Started</a></p>
</li>
<li>
<p>📚 <strong>Core Concepts</strong></p>
<p>The high-level explanations for building a better understand about the
important topics such as how to think about metrics-driven development, how the Ragas metrics work under the hood and synthetic dataset generation.</p>
<p><a href="concepts/index.md"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M13.22 19.03a.75.75 0 0 1 0-1.06L18.19 13H3.75a.75.75 0 0 1 0-1.5h14.44l-4.97-4.97a.749.749 0 0 1 .326-1.275.75.75 0 0 1 .734.215l6.25 6.25a.75.75 0 0 1 0 1.06l-6.25 6.25a.75.75 0 0 1-1.06 0"/></svg></span> Core Concepts</a></p>
</li>
<li>
<p>🛠️ <strong>How-to Guides</strong></p>
<p>Practical guides to help you achieve a specific goals. Take a look at these
guides to learn how to use Ragas to solve real-world problems.</p>
<p><a href="howtos/index.md"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M13.22 19.03a.75.75 0 0 1 0-1.06L18.19 13H3.75a.75.75 0 0 1 0-1.5h14.44l-4.97-4.97a.749.749 0 0 1 .326-1.275.75.75 0 0 1 .734.215l6.25 6.25a.75.75 0 0 1 0 1.06l-6.25 6.25a.75.75 0 0 1-1.06 0"/></svg></span> How-to Guides</a></p>
</li>
<li>
<p>📖 <strong>References</strong></p>
<p>Technical descriptions of how Ragas classes and methods work.</p>
<p><a href="references/index.md"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M13.22 19.03a.75.75 0 0 1 0-1.06L18.19 13H3.75a.75.75 0 0 1 0-1.5h14.44l-4.97-4.97a.749.749 0 0 1 .326-1.275.75.75 0 0 1 .734.215l6.25 6.25a.75.75 0 0 1 0 1.06l-6.25 6.25a.75.75 0 0 1-1.06 0"/></svg></span> References</a></p>
</li>
</ul>
</div>
<h1 id="introduction_1">Introduction</h1>
<p>Ragas is a framework that helps you evaluate your Retrieval Augmented Generation (RAG) pipelines. RAG denotes a class of LLM applications that use external data to augment the LLM’s context. There are existing tools and frameworks that help you build these pipelines but evaluating it and quantifying your pipeline performance can be hard. This is where Ragas (RAG Assessment) comes in.</p>
<div class="grid cards">
<ul>
<li>
<p>🚀 <strong>Get Started</strong></p>
<p>Learn the basics and become familiar with the Ragas metrics and how to evaluate
RAG pipelines with it, how to generate synthetic testsets to run evaluations
against and setting up online monitoring for your RAG apps.</p>
<p><a href="getstarted/index.md"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M13.22 19.03a.75.75 0 0 1 0-1.06L18.19 13H3.75a.75.75 0 0 1 0-1.5h14.44l-4.97-4.97a.749.749 0 0 1 .326-1.275.75.75 0 0 1 .734.215l6.25 6.25a.75.75 0 0 1 0 1.06l-6.25 6.25a.75.75 0 0 1-1.06 0"/></svg></span> Get Started</a></p>
</li>
<li>
<p>📚 <strong>Core Concepts</strong></p>
<p>The high-level explanations for building a better understand about the
important topics such as how to think about metrics-driven development, how the Ragas metrics work under the hood and synthetic dataset generation.</p>
<p><a href="concepts/index.md"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M13.22 19.03a.75.75 0 0 1 0-1.06L18.19 13H3.75a.75.75 0 0 1 0-1.5h14.44l-4.97-4.97a.749.749 0 0 1 .326-1.275.75.75 0 0 1 .734.215l6.25 6.25a.75.75 0 0 1 0 1.06l-6.25 6.25a.75.75 0 0 1-1.06 0"/></svg></span> Core Concepts</a></p>
</li>
<li>
<p>🛠️ <strong>How-to Guides</strong></p>
<p>Practical guides to help you achieve a specific goals. Take a look at these
guides to learn how to use Ragas to solve real-world problems.</p>
<p><a href="howtos/index.md"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M13.22 19.03a.75.75 0 0 1 0-1.06L18.19 13H3.75a.75.75 0 0 1 0-1.5h14.44l-4.97-4.97a.749.749 0 0 1 .326-1.275.75.75 0 0 1 .734.215l6.25 6.25a.75.75 0 0 1 0 1.06l-6.25 6.25a.75.75 0 0 1-1.06 0"/></svg></span> How-to Guides</a></p>
</li>
<li>
<p>📖 <strong>References</strong></p>
<p>Technical descriptions of how Ragas classes and methods work.</p>
<p><a href="references/index.md"><span class="twemoji"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M13.22 19.03a.75.75 0 0 1 0-1.06L18.19 13H3.75a.75.75 0 0 1 0-1.5h14.44l-4.97-4.97a.749.749 0 0 1 .326-1.275.75.75 0 0 1 .734.215l6.25 6.25a.75.75 0 0 1 0 1.06l-6.25 6.25a.75.75 0 0 1-1.06 0"/></svg></span> References</a></p>
</li>
</ul>
</div>












                
              </article>
            </div>
          
          
  <script>var tabs=__md_get("__tabs");if(Array.isArray(tabs))e:for(var set of document.querySelectorAll(".tabbed-set")){var labels=set.querySelector(".tabbed-labels");for(var tab of tabs)for(var label of labels.getElementsByTagName("label"))if(label.innerText.trim()===tab){var input=document.getElementById(label.htmlFor);input.checked=!0;continue e}}</script>

<script>var target=document.getElementById(location.hash.slice(1));target&&target.name&&(target.checked=target.name.startsWith("__tabbed_"))</script>
        </div>
        
          <button type="button" class="md-top md-icon" data-md-component="top" hidden>
  
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M13 20h-2V8l-5.5 5.5-1.42-1.42L12 4.16l7.92 7.92-1.42 1.42L13 8z"/></svg>
  Back to top
</button>
        
      </main>
      
        <footer class="md-footer">
  
    
      
      <nav class="md-footer__inner md-grid" aria-label="Footer" >
        
        
          
          <a href="example/" class="md-footer__link md-footer__link--next" aria-label="Next: Main">
            <div class="md-footer__title">
              <span class="md-footer__direction">
                Next
              </span>
              <div class="md-ellipsis">
                Main
              </div>
            </div>
            <div class="md-footer__button md-icon">
              
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M4 11v2h12l-5.5 5.5 1.42 1.42L19.84 12l-7.92-7.92L10.5 5.5 16 11z"/></svg>
            </div>
          </a>
        
      </nav>
    
  
  <div class="md-footer-meta md-typeset">
    <div class="md-footer-meta__inner md-grid">
      <div class="md-copyright">
  
  
    Made with
    <a href="https://squidfunk.github.io/mkdocs-material/" target="_blank" rel="noopener">
      Material for MkDocs
    </a>
  
</div>
      
    </div>
  </div>
</footer>
      
    </div>
    <div class="md-dialog" data-md-component="dialog">
      <div class="md-dialog__inner md-typeset"></div>
    </div>
    
      <div class="md-progress" data-md-component="progress" role="progressbar"></div>
    
    
    <script id="__config" type="application/json">{"base": ".", "features": ["content.tabs.link", "content.code.annotate", "content.code.copy", "announce.dismiss", "navigation.tabs", "navigation.instant", "navigation.instant.prefetch", "navigation.instant.progress", "navigation.path", "navigation.sections", "navigation.top", "navigation.tracking", "navigation.indexes", "navigation.footer", "search.suggest", "search.highlight"], "search": "assets/javascripts/workers/search.6ce7567c.min.js", "translations": {"clipboard.copied": "Copied to clipboard", "clipboard.copy": "Copy to clipboard", "search.result.more.one": "1 more on this page", "search.result.more.other": "# more on this page", "search.result.none": "No matching documents", "search.result.one": "1 matching document", "search.result.other": "# matching documents", "search.result.placeholder": "Type to start searching", "search.result.term.missing": "Missing", "select.version": "Select version"}, "version": {"alias": true, "provider": "mike"}}</script>
    
    
      <script src="assets/javascripts/bundle.525ec568.min.js"></script>
      
        <script src="extra/border.js"></script>
      
    
  </body>
</html>"""


# Navigate to the root and point to site/index.html
output_path = Path(__file__).resolve().parents[2] / "site" / "index.html"

# Create the directory if it doesn't exist
output_path.parent.mkdir(parents=True, exist_ok=True)

# Open the file and write content
with output_path.open("w", encoding='utf-8') as file:
    file.write(content)
