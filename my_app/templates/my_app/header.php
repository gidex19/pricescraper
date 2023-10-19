<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="facebook-domain-verification" content="7c6mn8ga142th1p6kjrsfppw9hs4gy" />
    <meta name="keywords" content="<?php echo get_theme_mod('seo_keywords'); ?>">
    <link rel="shortcut icon" href="<?php echo site_icon_url(); ?>">
    <?php wp_head(); 


    ?>
    <style><?php echo require_once('assets/build/css/style.php'); ?></style>
     <style><?php echo require_once('assets/build/css/responsive.php'); ?></style>
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-KZ30CTBXS5"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());

      gtag('config', 'G-KZ30CTBXS5');
    </script>
	<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1957707501303524"
     crossorigin="anonymous"></script>
	
	<script src="https://cdn.onesignal.com/sdks/OneSignalSDK.js" async=""></script>
	<script>
	  window.OneSignal = window.OneSignal || [];
	  OneSignal.push(function() {
		OneSignal.init({
		  appId: "702f54cb-a907-419d-9296-fadef40f1e8c",
		});
	  });
	</script>
	
	<style>
		 
		.mobile-only {
			display: none !important;
		}
		
		.margin-top {
			margin-top: 1em;
		}
		.margin-bottom {
			margin-bottom: 1em;
		}
		
		
	.ad-container {

		/* margin: 20px 0 20px 0;
		background: #fff8c0; //this is just for test purpose will remove later
		height: 600px;
		width: 300px;
		display: flex; */
/* 		align-items: center; */
		/* // justify-content: center; */
		background-color: #f0f0f0;
		
		 align-items: center;
		display: flex;
		flex-direction: column;
		justify-content: center;
		margin-bottom: 1.5em;
		margin-top: 1.5em;
	}

	.ad-container::before {
		content: 'advertisement';
		text-transform: uppercase;
		font-size: 9px;
		font-style: normal;
		font-weight: 314;
		letter-spacing: 0.388em;
		line-height: 14px;
		display: flex;
		justify-content: center;
		color: #000;
	}

	.ad-container .ad-container-inner {
		display: flex;
		align-items: center;
		justify-content: center;
		min-height: 250px;
	}
	/* } */

	.sticky-footer-ad {
        max-height: 100px;
        position: fixed;
        display: inline-block;
        bottom: 0;
        /* left: 0; */
        /* max-width: 100%; */
        width: 100%;
        padding: 10px 0;
        margin: 0;
        z-index: 9999;
        background-color: white;
        /* max-height: 90px; */
        box-shadow: inset 1px 5px 7px rgb(239 239 239 / 75%);
	}
	.sticky-footer-ad .ad-container {
        display: flex;
        align-items: center;
        justify-content: center;
        max-width: calc(100vw - 1.25rem);
    }
	.sticky-footer-ad .ad-containe::before {
        content: '';
    }
    
		@media screen and (min-width: 320px) and (max-width: 480px) {
			.desktop-only {
				display: none;
			}
			.mobile-only {
				display: block !important;
			}
		}
		
		@media screen and (max-width: 320px) {
			.desktop-only {
				display: none;
			}
			.mobile-only {
				display: block !important;
			}
		}
		
		.article-page article .post-content img{
			width: auto;
		}

</style>
	
</head>

<body>
    <nav class="navbar navbar-expand-xl navbar-light bg-light">
        <div class="container-fluid">
            <?php
                $custom_logo= get_theme_mod('custom_logo');
                $logo= wp_get_attachment_image_src($custom_logo, 'full');
                if (has_custom_logo()) {
                    echo '<a href="'.esc_url(get_bloginfo('url')).'" class="navbar-brand"><img style="width:250px;" src="'.esc_url( $logo[0]).'" alt="'.get_bloginfo('name').'"></a>';
                } 
            ?>
            <div class="search-btn">
                <a href="#" data-bs-toggle="modal" data-bs-target="#searchModal">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16">
                        <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z" />
                    </svg>
                </a>
               
            </div>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <?php
                    wp_nav_menu(
                        array(
                            'theme_location'=>'main_menu',
                            'menu_class'=>'navbar-nav',
                            'menu_id'=>'',
                            'container'=>'',
                            'walker' => new macho_bootstrap_walker()
                        )
                    );
                ?>
            </div>

            <div class="d-none d-lg-block d-xl-block">
                <a href="#" data-bs-toggle="modal" data-bs-target="#searchModal">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16">
                        <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z" />
                    </svg>
                </a>
                
            </div>

            <div class="modal fade" id="searchModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
                    <div class="modal-dialog">
                        <div class="modal-content">
                            <form method="get" action="<?php echo site_url(); ?>">
                               <input type="search" name="s" required>
                               <button class="searh">Search</button>
                           </form>
                        </div>
                    </div>
                </div>
        </div>
    </nav>
    <div class="secondary-mobile-nav">
        <?php
            wp_nav_menu(
                array(
                    'theme_location'=>'secondary_menu',
                    'menu_class'=>'',
                    'menu_id'=>'',
                    'container'=>''
                )
            );
        ?>
    </div>
	
	<?= do_shortcode("[adsense ad_id='leaderboard' placement='desktop']") ?>
