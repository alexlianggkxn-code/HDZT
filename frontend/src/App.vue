<script setup lang="ts">
import { ref } from "vue";
import { submitContactLead } from "./api";

const businessAreas = [
  {
    id: "agent",
    title: "脑电相关数据与智能体流程建设",
    summary:
      "围绕脑电相关记录、任务日志、语音视频资料和机器人训练过程，建立可追溯的数据整理与智能体流程，为后续标注、训练和内容生成提供稳定基础。",
    services: [
      "梳理实验记录、任务节点、样本来源和资料版本",
      "建立语音、视频、动作、场景说明等多模态资料字段",
      "设计资料入库、标签建议、复盘记录和版本维护流程",
    ],
    outcomes: ["数据结构表", "任务流程说明", "样本复盘记录"],
  },
  {
    id: "training",
    title: "机器人训练数据整理与动态标签",
    summary:
      "面向机械臂、小车、服务机器人等训练场景，把真实训练视频、动作记录、语音指令和场景描述整理成更清晰的训练样本，辅助后续模型训练与评估。",
    services: [
      "按训练任务拆分视频片段、动作阶段和关键事件",
      "结合语音指令、画面状态和任务结果补充动态标签",
      "记录样本质量、异常情况、复盘结论和可复用素材",
    ],
    outcomes: ["训练样本清单", "动态标签规范", "质量检查记录"],
  },
  {
    id: "companion",
    title: "陪伴机器人内容与交互素材建设",
    summary:
      "针对陪伴机器人在展厅、家庭、养老、教育和服务场景中的表达需求，整理对话脚本、语气风格、触发条件和反馈记录，让陪伴内容更自然、更可维护。",
    services: [
      "建立不同场景下的问候、提醒、解释、安抚和反馈话术",
      "梳理用户偏好、互动边界、禁用表达和人工接管规则",
      "沉淀内容版本，便于后续演示、试点和持续优化",
    ],
    outcomes: ["陪伴脚本库", "交互规则表", "内容版本记录"],
  },
];

const scenarios = [
  {
    title: "机器人训练实验室",
    description:
      "配合研发团队记录训练任务、设备状态、动作阶段和结果反馈，把零散实验资料整理成可复盘的数据资产。",
  },
  {
    title: "数据标注与质量复盘",
    description:
      "围绕样本来源、标签字段、标注口径和异常样本建立检查机制，减少后续训练和评估中的沟通成本。",
  },
  {
    title: "陪伴内容运营",
    description:
      "持续维护对话脚本、语气风格、触发条件和互动反馈，让机器人陪伴内容从一次性演示变成可迭代体系。",
  },
];

const deliverables = [
  "数据字段与标注规范",
  "机器人训练视频/动作标注样例",
  "场景化陪伴内容脚本",
  "数据复盘和质量检查记录",
  "可维护的后台内容与咨询记录",
];

const roadmap = [
  {
    title: "需求梳理",
    description: "确认机器人类型、训练任务、已有资料、试点场景和预期交付形式。",
  },
  {
    title: "资料整理",
    description: "汇总视频、语音、动作、记录表和场景说明，建立统一命名、字段和存档方式。",
  },
  {
    title: "标签与内容建设",
    description: "根据训练目标或陪伴场景补充动态标签、脚本内容、交互规则和质量状态。",
  },
  {
    title: "复盘交付",
    description: "输出可检查的样例、规范和记录，为后续数据库接入、后台维护和业务演示做准备。",
  },
];

const qualityPrinciples = [
  "不夸大当前能力，优先把真实资料整理清楚",
  "所有标签和脚本保留来源、版本和复盘记录",
  "交付内容面向后续维护，而不是一次性展示稿",
];

const contactForm = ref({
  name: "",
  organization: "",
  contact: "",
  interest: "general",
  message: "",
});
const isSubmittingContact = ref(false);
const contactStatus = ref("");
const contactError = ref("");

async function handleContactSubmit() {
  isSubmittingContact.value = true;
  contactStatus.value = "";
  contactError.value = "";

  try {
    const data = await submitContactLead(contactForm.value);
    contactStatus.value = data.message;
    contactForm.value = {
      name: "",
      organization: "",
      contact: "",
      interest: "general",
      message: "",
    };
  } catch {
    contactError.value = "提交暂时不可用，请稍后再试，或通过公开联系方式联系沪东智体。";
  } finally {
    isSubmittingContact.value = false;
  }
}
</script>

<template>
  <header class="site-header">
    <a class="brand" href="#top" aria-label="沪东智体首页">
      <img class="brand-logo" src="/images/hudongzhiti-logo.png" alt="沪东智体 logo" />
      <span>沪东智体</span>
    </a>
    <nav aria-label="主导航">
      <a href="#business">业务方向</a>
      <a href="#scenarios">应用场景</a>
      <a href="#deliverables">交付内容</a>
      <a href="#contact">合作咨询</a>
    </nav>
  </header>

  <main id="top">
    <section class="hero section-shell">
      <div class="hero-copy">
        <div class="hero-brand">
          <img src="/images/hudongzhiti-logo.png" alt="" />
          <span>沪东智体人工智能科技（上海）有限公司</span>
        </div>
        <h1>面向机器人训练与陪伴内容的数据整理服务</h1>
        <p>
          沪东智体把真实研发场景中的语音、视频、动作、记录表和互动反馈，整理成可复盘、可维护、可迭代的数据与内容资产。
        </p>
        <div class="hero-actions">
          <a class="primary-link" href="#business">查看业务方向</a>
          <a class="secondary-link" href="#contact">提交合作咨询</a>
        </div>
        <div class="capability-strip" aria-label="核心能力摘要">
          <span>真实训练资料整理</span>
          <span>多模态标签流程</span>
          <span>陪伴内容体系维护</span>
        </div>
      </div>
      <div class="hero-visual" aria-label="机器人训练数据标注与研发工作位场景">
        <img
          src="/images/hero-eeg-robotics.png?v=realistic-2"
          alt="机器人训练数据标注与研发工作位场景"
        />
      </div>
    </section>

    <section class="company-intro">
      <div class="section-shell company-intro-inner">
        <div>
          <h2>公司定位</h2>
          <p>
            沪东智体聚焦机器人训练过程中的资料整理、标签体系和陪伴内容建设。首版官网强调可落地的协作方式：把已有实验材料、训练样本和陪伴内容变成结构清晰、责任明确、后续可维护的项目资料。
          </p>
        </div>
        <ul class="quality-list">
          <li v-for="item in qualityPrinciples" :key="item">{{ item }}</li>
        </ul>
      </div>
    </section>

    <section id="business" class="section-shell business-section">
      <div class="section-heading">
        <h2>业务方向</h2>
        <p>
          当前官网围绕三类工作展开：脑电相关数据与智能体流程、机器人训练动态标签、陪伴机器人内容建设。每一类都以真实资料、清晰字段和可复盘交付为核心。
        </p>
      </div>
      <div class="business-list">
        <article v-for="area in businessAreas" :id="area.id" :key="area.id" class="business-item">
          <div>
            <h3>{{ area.title }}</h3>
            <p>{{ area.summary }}</p>
          </div>
          <div class="business-detail">
            <h4>服务内容</h4>
            <ul>
              <li v-for="service in area.services" :key="service">{{ service }}</li>
            </ul>
          </div>
          <div class="outcome-row" aria-label="可形成成果">
            <span v-for="outcome in area.outcomes" :key="outcome">{{ outcome }}</span>
          </div>
        </article>
      </div>
    </section>

    <section id="scenarios" class="scenario-section">
      <div class="section-shell">
        <div class="section-heading">
          <h2>应用场景</h2>
          <p>
            页面内容围绕真实工作流程展开，适合用于研发团队资料整理、训练数据协作、陪伴机器人试点和后续项目沟通。
          </p>
        </div>
        <div class="scenario-grid">
          <article v-for="scenario in scenarios" :key="scenario.title" class="scenario-item">
            <h3>{{ scenario.title }}</h3>
            <p>{{ scenario.description }}</p>
          </article>
        </div>
      </div>
    </section>

    <section id="deliverables" class="section-shell deliverables-section">
      <div class="section-heading">
        <h2>可交付内容</h2>
        <p>
          合作成果不只停留在页面展示，而是沉淀为可检查、可维护、可继续接入数据库和后台系统的资料包。
        </p>
      </div>
      <div class="deliverables-layout">
        <ul class="deliverable-list">
          <li v-for="item in deliverables" :key="item">{{ item }}</li>
        </ul>
        <div class="process-panel">
          <h3>合作流程</h3>
          <ol>
            <li v-for="item in roadmap" :key="item.title">
              <strong>{{ item.title }}</strong>
              <span>{{ item.description }}</span>
            </li>
          </ol>
        </div>
      </div>
    </section>

    <section class="roadmap">
      <div class="section-shell roadmap-inner">
        <div class="section-heading">
          <h2>技术路线</h2>
          <p>
            从真实训练资料出发，通过数据结构、标注流程、内容后台和复盘记录，把研发过程逐步沉淀为可维护的业务资产。
          </p>
        </div>
        <ol>
          <li v-for="item in roadmap" :key="item.title">
            <strong>{{ item.title }}</strong>
            <span>{{ item.description }}</span>
          </li>
        </ol>
      </div>
    </section>

    <section id="contact" class="contact-section">
      <div class="section-shell contact-inner">
        <div class="section-heading">
          <h2>合作咨询</h2>
          <p>
            如果你有机器人训练数据、标注流程、陪伴内容或官网展示需求，可以留下方向和现有资料情况，后续通过后台记录统一跟进。
          </p>
        </div>

        <form class="contact-form" @submit.prevent="handleContactSubmit">
          <label>
            <span>姓名</span>
            <input v-model="contactForm.name" required minlength="2" type="text" placeholder="请输入姓名" />
          </label>
          <label>
            <span>机构/公司</span>
            <input v-model="contactForm.organization" type="text" placeholder="可选" />
          </label>
          <label>
            <span>联系方式</span>
            <input
              v-model="contactForm.contact"
              required
              minlength="5"
              type="text"
              placeholder="邮箱、电话或微信"
            />
          </label>
          <label>
            <span>咨询方向</span>
            <select v-model="contactForm.interest">
              <option value="general">综合咨询</option>
              <option value="agent">数据与智能体流程</option>
              <option value="training">机器人训练</option>
              <option value="companion">机器人陪伴</option>
            </select>
          </label>
          <label class="message-field">
            <span>需求描述</span>
            <textarea
              v-model="contactForm.message"
              required
              minlength="10"
              rows="5"
              placeholder="请简单描述合作场景、已有资料、技术需求或想了解的问题"
            ></textarea>
          </label>
          <button type="submit" :disabled="isSubmittingContact">
            {{ isSubmittingContact ? "提交中" : "提交咨询" }}
          </button>
          <p v-if="contactStatus" class="form-success" role="status">{{ contactStatus }}</p>
          <p v-if="contactError" class="form-error" role="alert">{{ contactError }}</p>
        </form>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="footer-brand">
      <img src="/images/hudongzhiti-logo.png" alt="" />
      <strong>沪东智体人工智能科技（上海）有限公司</strong>
    </div>
    <span>面向机器人训练、数据标注与陪伴内容建设</span>
  </footer>
</template>
