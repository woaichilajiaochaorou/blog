import { defineConfig } from 'vitepress'

export default defineConfig({
  title: "Shannon's Blog",
  description: '个人技术博客',
  lang: 'zh-CN',
  cleanUrls: true,
  head: [
    ['meta', { name: 'author', content: 'Shannon' }],
  ],
  themeConfig: {
    siteTitle: "Shannon's Blog",
    nav: [
      { text: '首页', link: '/' },
      { text: '文章', link: '/posts/' },
      { text: '关于', link: '/about' },
    ],
    sidebar: {
      '/posts/': [
        {
          text: '技术文章',
          collapsed: false,
          items: [
            { text: 'VitePress + Oracle Cloud 博客搭建', link: '/posts/vitepress-oracle-cloud' },
            { text: 'Hello World', link: '/posts/hello-world' },
          ],
        },
      ],
    },
    socialLinks: [
      { icon: 'github', link: 'https://github.com/shannonyan' },
    ],
    footer: {
      message: 'Powered by VitePress | Deployed on Oracle Cloud',
      copyright: 'Copyright © 2026 Shannon',
    },
    outline: { level: [2, 3], label: '目录' },
    lastUpdated: { text: '最后更新于' },
    search: {
      provider: 'local',
      options: {
        translations: {
          button: { buttonText: '搜索', buttonAriaLabel: '搜索' },
          modal: { noResultsText: '没有找到相关结果', resetButtonTitle: '清除' },
        },
      },
    },
    docFooter: { prev: '上一篇', next: '下一篇' },
  },
})
