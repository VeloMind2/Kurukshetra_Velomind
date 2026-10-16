import { useEffect, useState, type ReactNode } from "react";

type IconName =
  | "activity"
  | "arrow"
  | "bell"
  | "book"
  | "brain"
  | "check"
  | "chevron"
  | "clock"
  | "code"
  | "dashboard"
  | "flame"
  | "flask"
  | "grid"
  | "language"
  | "map"
  | "menu"
  | "search"
  | "settings"
  | "shield"
  | "spark"
  | "target"
  | "team"
  | "x";

function Icon({ name, size = 18 }: { name: IconName; size?: number }) {
  const paths: Record<IconName, ReactNode> = {
    activity: <><path d="M4 12h3l2-6 4 12 2-6h5" /></>,
    arrow: <><path d="M5 12h14M13 6l6 6-6 6" /></>,
    bell: <><path d="M18 8a6 6 0 0 0-12 0c0 7-3 7-3 9h18c0-2-3-2-3-9M10 21h4" /></>,
    book: <><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V4H6.5A2.5 2.5 0 0 0 4 6.5v13Z" /><path d="M8 7h8M8 11h6" /></>,
    brain: <><path d="M9.5 4.5A3 3 0 0 0 6 8v1a3 3 0 0 0 0 6v1a3 3 0 0 0 3.5 3M14.5 4.5A3 3 0 0 1 18 8v1a3 3 0 0 1 0 6v1a3 3 0 0 1-3.5 3M12 4v16M8 10h4M12 14h4" /></>,
    check: <><path d="m5 12 4 4L19 6" /></>,
    chevron: <><path d="m9 18 6-6-6-6" /></>,
    clock: <><circle cx="12" cy="12" r="9" /><path d="M12 7v5l3 2" /></>,
    code: <><path d="m8 9-4 3 4 3M16 9l4 3-4 3M14 5l-4 14" /></>,
    dashboard: <><rect x="3" y="3" width="7" height="7" rx="1" /><rect x="14" y="3" width="7" height="7" rx="1" /><rect x="3" y="14" width="7" height="7" rx="1" /><rect x="14" y="14" width="7" height="7" rx="1" /></>,
    flame: <><path d="M12 22c4 0 7-3 7-7 0-3-1.5-5.5-4-8 .2 3-1 4-2 4-1.5 0-2-2-1-6-4 2.5-7 6-7 10 0 4 3 7 7 7Z" /><path d="M9 18c0-2 1-3 3-5 0 2 3 2 3 5" /></>,
    flask: <><path d="M9 3h6M10 3v6l-5 9a2 2 0 0 0 2 3h10a2 2 0 0 0 2-3l-5-9V3M7.5 15h9" /></>,
    grid: <><path d="M4 4h6v6H4zM14 4h6v6h-6zM4 14h6v6H4zM14 14h6v6h-6z" /></>,
    language: <><circle cx="12" cy="12" r="9" /><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18" /></>,
    map: <><path d="m3 6 5-3 8 3 5-3v15l-5 3-8-3-5 3V6ZM8 3v15M16 6v15" /></>,
    menu: <><path d="M4 7h16M4 12h16M4 17h16" /></>,
    search: <><circle cx="11" cy="11" r="7" /><path d="m20 20-4-4" /></>,
    settings: <><circle cx="12" cy="12" r="3" /><path d="M19.4 15a1.7 1.7 0 0 0 .3 1.9l.1.1-2.8 2.8-.1-.1a1.7 1.7 0 0 0-1.9-.3 1.7 1.7 0 0 0-1 1.6v.2h-4V21a1.7 1.7 0 0 0-1-1.6 1.7 1.7 0 0 0-1.9.3l-.1.1L4.2 17l.1-.1a1.7 1.7 0 0 0 .3-1.9A1.7 1.7 0 0 0 3 14H3v-4h.2a1.7 1.7 0 0 0 1.5-1 1.7 1.7 0 0 0-.3-1.9L4.2 7 7 4.2l.1.1a1.7 1.7 0 0 0 1.9.3A1.7 1.7 0 0 0 10 3V3h4v.2a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.9-.3l.1-.1L19.8 7l-.1.1a1.7 1.7 0 0 0-.3 1.9 1.7 1.7 0 0 0 1.6 1h.2v4H21a1.7 1.7 0 0 0-1.6 1Z" /></>,
    shield: <><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10Z" /><path d="m9 12 2 2 4-4" /></>,
    spark: <><path d="m12 3 1.3 4.2L17 9l-3.7 1.8L12 15l-1.3-4.2L7 9l3.7-1.8L12 3ZM5 15l.8 2.2L8 18l-2.2.8L5 21l-.8-2.2L2 18l2.2-.8L5 15ZM19 14l.6 1.4L21 16l-1.4.6L19 18l-.6-1.4L17 16l1.4-.6L19 14Z" /></>,
    target: <><circle cx="12" cy="12" r="9" /><circle cx="12" cy="12" r="5" /><circle cx="12" cy="12" r="1" /></>,
    team: <><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2M9 11a4 4 0 1 0 0-8M22 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8" /></>,
    x: <><path d="M6 6l12 12M18 6 6 18" /></>,
  };

  return (
    <svg aria-hidden="true" width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
      {paths[name]}
    </svg>
  );
}

const navItems: { label: string; icon: IconName }[] = [
  { label: "Dashboard", icon: "dashboard" },
  { label: "Adaptive Assessment", icon: "target" },
  { label: "Concept Map", icon: "map" },
  { label: "Learning Autopsy", icon: "brain" },
  { label: "Bug Mutation Lab", icon: "flask" },
  { label: "Language Comparison", icon: "language" },
  { label: "Integrity Timeline", icon: "shield" },
  { label: "Trainer Dashboard", icon: "team" },
  { label: "Settings", icon: "settings" },
];

const stats: { label: string; value: string; detail: string; progress: number; icon: IconName; tone: string }[] = [
  { label: "Overall Mastery", value: "68%", detail: "+6% this week", progress: 68, icon: "target", tone: "green" },
  { label: "Questions Solved", value: "42", detail: "7 this week", progress: 76, icon: "code", tone: "coral" },
  { label: "Concepts Mastered", value: "8", detail: "of 12 concepts", progress: 66, icon: "brain", tone: "lavender" },
  { label: "Learning Streak", value: "5 Days", detail: "Personal best: 12", progress: 42, icon: "flame", tone: "sage" },
];

const concepts = [
  { name: "Variables", state: "mastered", score: "92%" },
  { name: "Conditions", state: "mastered", score: "84%" },
  { name: "Loops", state: "weak", score: "48%" },
  { name: "Arrays", state: "progress", score: "64%" },
  { name: "Functions", state: "locked", score: "Next" },
];

const activities = [
  { name: "Loop Logic", note: "Assessment · 18 min", status: "Needs Practice", tone: "coral", icon: "code" as IconName },
  { name: "Conditional Statements", note: "Concept drill · 12 min", status: "Mastered", tone: "green", icon: "check" as IconName },
  { name: "Array Traversal", note: "Practice set · 9 min", status: "In Progress", tone: "lavender", icon: "activity" as IconName },
];

function Brand() {
  return (
    <div className="brand">
      <span className="brand-mark"><Icon name="spark" size={22} /></span>
      <span>SkillTrace <b>AI</b></span>
    </div>
  );
}

function Sidebar({
  active,
  onNavigate,
  open,
  onClose,
}: {
  active: string;
  onNavigate: (label: string) => void;
  open: boolean;
  onClose: () => void;
}) {
  return (
    <>
      <div className={`sidebar-backdrop ${open ? "is-open" : ""}`} onClick={onClose} />
      <aside className={`sidebar ${open ? "is-open" : ""}`}>
        <div className="sidebar-head">
          <Brand />
          <button className="icon-button sidebar-close" onClick={onClose} aria-label="Close navigation"><Icon name="x" /></button>
        </div>
        <nav className="sidebar-nav" aria-label="Main navigation">
          <span className="nav-label">Workspace</span>
          {navItems.map((item) => (
            <button
              key={item.label}
              className={`nav-item ${active === item.label ? "active" : ""}`}
              onClick={() => onNavigate(item.label)}
            >
              <Icon name={item.icon} />
              <span>{item.label}</span>
              {item.label === "Learning Autopsy" && <span className="nav-dot" />}
            </button>
          ))}
        </nav>
        <div className="sidebar-insight">
          <span className="insight-icon"><Icon name="spark" /></span>
          <div>
            <strong>Weekly insight</strong>
            <p>You’re 2 sessions away from your learning goal.</p>
          </div>
          <div className="mini-progress"><span style={{ width: "72%" }} /></div>
        </div>
        <div className="sidebar-user">
          <span className="avatar">AM</span>
          <div><strong>Alex Morgan</strong><small>Student plan</small></div>
          <Icon name="chevron" size={15} />
        </div>
      </aside>
    </>
  );
}

function Topbar({
  active,
  onMenu,
  onNotifications,
  onProfile,
  profileOpen,
}: {
  active: string;
  onMenu: () => void;
  onNotifications: () => void;
  onProfile: () => void;
  profileOpen: boolean;
}) {
  return (
    <header className="topbar">
      <div className="topbar-left">
        <button className="icon-button mobile-menu" onClick={onMenu} aria-label="Open navigation"><Icon name="menu" /></button>
        <div className="breadcrumb"><span>Home</span><Icon name="chevron" size={13} /><strong>{active}</strong></div>
      </div>
      <div className="topbar-actions">
        <label className="search">
          <Icon name="search" size={17} />
          <input aria-label="Search" placeholder="Search concepts, challenges..." />
          <kbd>⌘ K</kbd>
        </label>
        <button className="icon-button notification-button" onClick={onNotifications} aria-label="View notifications">
          <Icon name="bell" />
          <span className="notification-dot" />
        </button>
        <div className="profile-wrap">
          <button className="profile-button" onClick={onProfile} aria-expanded={profileOpen}>
            <span className="avatar">AM</span>
            <span className="profile-copy"><strong>Alex Morgan</strong><small>Student</small></span>
            <Icon name="chevron" size={14} />
          </button>
          {profileOpen && (
            <div className="profile-menu">
              <strong>Alex Morgan</strong>
              <small>alex@skilltrace.demo</small>
              <button>View profile</button>
              <button>Account settings</button>
            </div>
          )}
        </div>
      </div>
    </header>
  );
}

function StatCard({ stat }: { stat: typeof stats[number] }) {
  return (
    <article className="stat-card">
      <div className="stat-top">
        <span className={`stat-icon ${stat.tone}`}><Icon name={stat.icon} /></span>
        <span className="demo-pill">Demo data</span>
      </div>
      <p>{stat.label}</p>
      <div className="stat-value-row"><strong>{stat.value}</strong><span>{stat.detail}</span></div>
      <div className="progress-track"><span className={stat.tone} style={{ width: `${stat.progress}%` }} /></div>
    </article>
  );
}

function ConceptMap({ onSelect }: { onSelect: (name: string) => void }) {
  return (
    <section className="card concept-card">
      <div className="section-head">
        <div><span className="eyebrow">Learning path</span><h2>Concept mastery map</h2></div>
        <button className="text-button" onClick={() => onSelect("Full concept map")}>View full map <Icon name="arrow" size={15} /></button>
      </div>
      <div className="concept-legend">
        <span><i className="legend-dot mastered" />Mastered</span>
        <span><i className="legend-dot progress" />In progress</span>
        <span><i className="legend-dot weak" />Needs focus</span>
      </div>
      <div className="concept-flow">
        <div className="flow-line" />
        {concepts.map((concept, index) => (
          <button key={concept.name} className={`concept-node ${concept.state}`} onClick={() => onSelect(concept.name)}>
            {concept.name === "Loops" && <span className="focus-label">Recommended focus</span>}
            <span className="node-circle">{concept.state === "mastered" ? <Icon name="check" /> : index + 1}</span>
            <strong>{concept.name}</strong>
            <small>{concept.score}</small>
          </button>
        ))}
      </div>
      <div className="map-insight">
        <span><Icon name="spark" /></span>
        <p><strong>Your learning path adapted.</strong> Strengthen loop boundaries before moving into nested array operations.</p>
      </div>
    </section>
  );
}

function NextChallenge({ onStart }: { onStart: () => void }) {
  return (
    <section className="challenge-card">
      <div className="challenge-glow" />
      <div className="challenge-top"><span><Icon name="spark" size={16} /> Your next challenge</span><span className="match-pill">94% skill match</span></div>
      <div className="challenge-icon"><Icon name="code" size={24} /></div>
      <h2>Find the hidden loop boundary bug</h2>
      <p>You have repeatedly made off-by-one errors. Test your understanding with a new problem.</p>
      <div className="challenge-meta">
        <span><i className="difficulty-dot" /> Intermediate</span>
        <span><Icon name="clock" size={15} /> 15 min</span>
      </div>
      <button className="light-button" onClick={onStart}>Start Challenge <Icon name="arrow" size={16} /></button>
    </section>
  );
}

function AutopsyCard({ onAction }: { onAction: () => void }) {
  return (
    <section className="card autopsy-card">
      <div className="section-head compact">
        <div><span className="eyebrow">Learning autopsy</span><h2>Loop Boundary Confusion</h2></div>
        <span className="confidence"><i /> Moderate confidence</span>
      </div>
      <p className="support-copy">A recurring pattern may be slowing you down. This is common and highly fixable.</p>
      <div className="evidence-list">
        <div><span className="evidence-icon"><Icon name="activity" /></span><p><small>Pattern detected</small><strong>Incorrect loop condition</strong></p></div>
        <div><span className="evidence-icon coral"><Icon name="code" /></span><p><small>Evidence from attempts</small><strong>Used <code>&lt;</code> where <code>&lt;=</code> was required</strong></p></div>
        <div><span className="evidence-icon sage"><Icon name="spark" /></span><p><small>Recommended next step</small><strong>Try a mutation challenge</strong></p></div>
      </div>
      <button className="outline-button" onClick={onAction}>Explore this insight <Icon name="arrow" size={15} /></button>
    </section>
  );
}

function ProgressChart() {
  return (
    <section className="card progress-card">
      <div className="section-head">
        <div><span className="eyebrow">Learning progress</span><h2>Mastery improvement</h2></div>
        <div className="trend-badge">↗ 12% this week</div>
      </div>
      <div className="chart-wrap" aria-label="Mastery increased from 42 to 68 percent over seven days">
        <div className="y-axis"><span>80%</span><span>60%</span><span>40%</span><span>20%</span></div>
        <div className="chart">
          <div className="grid-lines"><i /><i /><i /><i /></div>
          <svg viewBox="0 0 700 190" preserveAspectRatio="none" aria-hidden="true">
            <defs>
              <linearGradient id="chartFill" x1="0" y1="0" x2="0" y2="1">
                <stop offset="0%" stopColor="#173B35" stopOpacity=".18" />
                <stop offset="100%" stopColor="#173B35" stopOpacity="0" />
              </linearGradient>
            </defs>
            <path className="chart-area" d="M0 155 C70 150 85 130 117 132 S205 138 233 111 S325 102 350 95 S440 83 467 67 S560 60 583 43 S660 38 700 22 L700 190 L0 190Z" />
            <path className="chart-line" d="M0 155 C70 150 85 130 117 132 S205 138 233 111 S325 102 350 95 S440 83 467 67 S560 60 583 43 S660 38 700 22" />
            {[["0","155"],["117","132"],["233","111"],["350","95"],["467","67"],["583","43"],["700","22"]].map(([cx, cy]) => <circle key={cx} cx={cx} cy={cy} r="4.5" />)}
          </svg>
          <div className="x-axis"><span>Mon</span><span>Tue</span><span>Wed</span><span>Thu</span><span>Fri</span><span>Sat</span><span>Sun</span></div>
        </div>
      </div>
    </section>
  );
}

function RecentActivity() {
  return (
    <section className="card activity-card">
      <div className="section-head"><div><span className="eyebrow">This week</span><h2>Recent activity</h2></div><button className="more-button" aria-label="More activity options">•••</button></div>
      <div className="activity-list">
        {activities.map((item) => (
          <button className="activity-item" key={item.name}>
            <span className={`activity-icon ${item.tone}`}><Icon name={item.icon} /></span>
            <span className="activity-copy"><strong>{item.name}</strong><small>{item.note}</small></span>
            <span className={`status ${item.tone}`}>{item.status}</span>
            <Icon name="chevron" size={15} />
          </button>
        ))}
      </div>
      <button className="text-button activity-link">View all activity <Icon name="arrow" size={15} /></button>
    </section>
  );
}

function Dashboard({
  onStart,
  onConcept,
  onNavigate,
}: {
  onStart: () => void;
  onConcept: (name: string) => void;
  onNavigate: (page: string) => void;
}) {
  return (
    <>
      <div className="hero">
        <div>
          <span className="welcome"><i /> Monday, 24 June</span>
          <h1>Your code. Your thinking.<br /><em>Your growth.</em></h1>
          <p>Understand your mistakes and build stronger coding fundamentals.</p>
        </div>
        <button className="primary-button" onClick={() => onNavigate("Adaptive Assessment")}><span><Icon name="book" /></span>Continue Learning<Icon name="arrow" size={16} /></button>
      </div>
      <div className="stats-grid">{stats.map((stat) => <StatCard key={stat.label} stat={stat} />)}</div>
      <div className="main-grid">
        <ConceptMap onSelect={onConcept} />
        <NextChallenge onStart={onStart} />
        <AutopsyCard onAction={() => onNavigate("Learning Autopsy")} />
        <ProgressChart />
        <RecentActivity />
      </div>
    </>
  );
}

function PlaceholderPage({ page, onBack }: { page: string; onBack: () => void }) {
  return (
    <div className="placeholder-page">
      <span className="placeholder-icon"><Icon name={navItems.find((item) => item.label === page)?.icon ?? "spark"} size={30} /></span>
      <span className="eyebrow">SkillTrace workspace</span>
      <h1>{page}</h1>
      <p>This interactive prototype keeps the dashboard as the primary experience. The {page.toLowerCase()} workspace is ready for the next hackathon iteration.</p>
      <button className="primary-button" onClick={onBack}><Icon name="dashboard" />Return to Dashboard</button>
    </div>
  );
}

function Assessment({ onBack }: { onBack: () => void }) {
  const [selected, setSelected] = useState<number | null>(null);
  return (
    <div className="assessment-page">
      <button className="back-button" onClick={onBack}>← Back to dashboard</button>
      <div className="assessment-shell">
        <div className="assessment-head">
          <div><span className="eyebrow">Adaptive assessment · Question 1 of 5</span><h1>Find the hidden loop boundary bug</h1></div>
          <span className="timer"><Icon name="clock" /> 14:58</span>
        </div>
        <p>Which change ensures every item in the array is processed without reading beyond its boundary?</p>
        <pre><code>{`const scores = [72, 88, 91, 64];\n\nfor (let i = 0; i <= scores.length; i++) {\n  console.log(scores[i]);\n}`}</code></pre>
        <div className="answers">
          {["Change i <= scores.length to i < scores.length", "Change i++ to ++i", "Change i = 0 to i = 1", "No change is needed"].map((answer, index) => (
            <button className={selected === index ? "selected" : ""} onClick={() => setSelected(index)} key={answer}><span>{String.fromCharCode(65 + index)}</span>{answer}</button>
          ))}
        </div>
        <button className="primary-button assessment-submit" disabled={selected === null}>Check answer <Icon name="arrow" size={16} /></button>
      </div>
    </div>
  );
}

function Toast({ message, onClose }: { message: string; onClose: () => void }) {
  useEffect(() => {
    const timer = window.setTimeout(onClose, 3200);
    return () => window.clearTimeout(timer);
  }, [onClose]);
  return <div className="toast"><span><Icon name="bell" /></span><div><strong>SkillTrace update</strong><p>{message}</p></div><button onClick={onClose} aria-label="Dismiss"><Icon name="x" size={15} /></button></div>;
}

export default function App() {
  const [active, setActive] = useState("Dashboard");
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [profileOpen, setProfileOpen] = useState(false);
  const [toast, setToast] = useState("");
  const [assessment, setAssessment] = useState(false);

  const navigate = (page: string) => {
    setActive(page);
    setAssessment(false);
    setSidebarOpen(false);
    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  const selectConcept = (name: string) => {
    if (name === "Full concept map") navigate("Concept Map");
    else setToast(`${name} details opened. Your latest mastery signal is ready to review.`);
  };

  return (
    <div className="app-shell">
      <Sidebar active={active} onNavigate={navigate} open={sidebarOpen} onClose={() => setSidebarOpen(false)} />
      <div className="workspace">
        <Topbar
          active={assessment ? "Adaptive Assessment" : active}
          onMenu={() => setSidebarOpen(true)}
          onNotifications={() => setToast("You have 2 new insights: your loop accuracy improved by 8%.")}
          onProfile={() => setProfileOpen(!profileOpen)}
          profileOpen={profileOpen}
        />
        <main>
          {assessment ? (
            <Assessment onBack={() => setAssessment(false)} />
          ) : active === "Dashboard" ? (
            <Dashboard onStart={() => setAssessment(true)} onConcept={selectConcept} onNavigate={navigate} />
          ) : (
            <PlaceholderPage page={active} onBack={() => navigate("Dashboard")} />
          )}
        </main>
      </div>
      {toast && <Toast message={toast} onClose={() => setToast("")} />}
    </div>
  );
}
