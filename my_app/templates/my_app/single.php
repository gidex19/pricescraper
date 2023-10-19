<?php

get_header();
if (have_posts()) : the_post(); ?> <header class="breadcrumb-header">
        <ul>
            <li><a href="<?= site_url(); ?>">Home</a></li>
            <li class="divider"><a href="#">|</a></li>
            <li><a href="#"><?= the_title(); ?></a></li>
        </ul>
    </header>
    <content class="article-page">
        <div class="container">
            <div class="row">
                <div class="col-lg-9">
                    <article>
                        <?php 
                            if(has_post_format('video')) { 
                                $youtube_id = get_post_meta(get_the_ID(), '_youtube_id', true);
                                echo '<div class="video-container">
                                    <iframe style="width: 100%; height: 500px;" src="https://www.youtube.com/embed/'.$youtube_id.'" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                                </div>';
                            }else {

                            ?>
                        <figure>
                            <?php echo get_thumbnail(['post_id' => get_the_ID(), 'size' => 'full', 'classes' => 'post-image']); ?>
                        </figure> <?php if (get_the_post_thumbnail_caption() != "") {
                                        echo '<div 
                                class="caption"><p>' . get_the_post_thumbnail_caption() . '</p></div>';
                                    }
                                }?> <h1 class="post-title"><?php the_title(); ?></h1>
                        <div class="post-meta">
                            <p class="post-author">By <a href="<?php echo
                                                                get_author_posts_url(get_the_author_meta('ID')); ?>"><?php the_author(); ?></a> </p>
                            <p class="post-date"><?php
                                                    the_date(); ?></p>
                            <div class="social-share">
                                <?php echo social_share(); ?> </div>
                        </div> 
                        <?= do_shortcode("[adsense ad_id='responsive_1']") ?> <div class="post-content">
                            <?php
                            add_filter('the_content', 'insert_read_also');

                            function insert_read_also($content)
                            {
                                $tags = get_the_tags();

                                if (!empty($tags)) {

                                    foreach ($tags as $individual_tag) $tag_ids[] = $individual_tag->term_id;
                                    //  query_posts(['category_name'=>'featured', 'posts_per_page'=>5, 'post__not_in'=>$exclude_id]);
                                    $read_also = query_posts(
                                        array(
                                            'tag__in' => $tag_ids,
                                            'post__not_in' => array(get_the_ID()),
                                            'posts_per_page' => 3,
                                        )
                                    );
                                    // if ( empty( $read_also) ) break;

                                    $read_also_content = ' <div class="related-article"> <h3>Related News</h3> <ul>';

                                    foreach ($read_also as $post) {
                                        $read_also_content .= '<li><a href="' . get_the_permalink($post->ID) . '?utm_source=auto-read-also&utm_medium=web">' . $post->post_title . '</a></li>';
                                    }

                                    $read_also_content .= '</ul> </div>';

                                    $read_also_content = (empty($read_also)) ? ' ' : $read_also_content;

                                    return insert_after_paragraph($read_also_content, $content);
                                }
                                return $content;
                            }

                            the_content();

                            ?>

                        </div> <?= do_shortcode("[adsense ad_id='multiplex']") ?> <?php if (comments_open()) : ?>
                            <div class="comment-box">
                                <div id="disqus_thread"></div>
                                <script>
                                    var disqus_config = function() {
                                        this.page.url = "<?=
                                                                                        get_the_permalink(); ?>";
                                        this.page.identifier = <?= get_the_ID(); ?>
                                    };

                                    (function() { // DON'T EDIT BELOW THIS LINE var d = document, s = d.createElement('script'); s.src = 
                                        'https://the-nigerian-observer-1.disqus.com/embed.js';
                                        s.setAttribute('data-timestamp', +new Date());
                                        (d.head || d.body).appendChild(s);
                                    })();
                                </script>
                            </div> <?php endif; ?>
                    </article>
                </div>
                <div class="col-lg-3">
                    <aside> <?php if (is_active_sidebar('article_page_sidebar')) {
                                dynamic_sidebar('article_page_sidebar');
                            }
                            ?> </aside>
                </div>
            </div>
        </div>
    </content> <?php endif;
            if (is_active_sidebar('article_page_widget_section')) {
                dynamic_sidebar('article_page_widget_section');
            }
                ?> <?php get_footer(); ?>