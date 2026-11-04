const OFFICIAL="https://gttc.karnataka.gov.in/9/belgaum/en";
const PLACEMENT="https://gttc.karnataka.gov.in/153/placement-and-entrepreneurs/en";
const STOP=new Set(["a","an","the","is","are","was","were","to","of","for","in","on","at","do","does","did","can","could","would","what","when","where","how","why","please","tell","me","about","my","our","your","i","we","you","and","or","from","with","this","that"]);
const POS=new Set(["good","great","excellent","thanks","thank","happy","nice","helpful","awesome"]);
const NEG=new Set(["bad","poor","wrong","confused","sad","problem","difficult","not"]);
const intents=[
["short_term",["short term","short-term","cnc","cmm","autocad","solid works","catia","cad-cam"]],
["timings",["working hours","college timings","college time","collage time","when college starts","when college closes","open","close"]],
["courses",["courses","course","departments","branches","diploma","tool die","precision","automation","robotics"]],
["aiml",["aiml","artificial intelligence","machine learning"]],
["admission",["admission","apply","application","eligibility","join"]],
["fees",["fee","fees","cost","price","semester"]],
["contact",["contact","phone","telephone","call","mobile","email"]],
["website",["website","official site","web site","link"]],
["library",["library"]],
["exam",["exam","examination","test","internal assessment"]],
["location",["address","location","where","udyambag","belgaum","belagavi"]],
["principal",["principal","principle","head of college","head of institution","who is the principal"]],
["placement",["placement","placements","job","recruit","placement company","placement companies","companies hire","companies recruit","which companies","placement information"]]
];
const COURSE_CARDS=[
 {title:"Diploma in Tool and Die Making",meta:"3+1 years • ₹13,750 per semester • Intake 60"},
 {title:"Diploma in Precision Manufacturing",meta:"3+1 years • ₹13,750 per semester • Intake 30"},
 {title:"Diploma in Automation and Robotics",meta:"3+1 years • ₹13,750 per semester • Intake 60"},
 {title:"Diploma in Artificial Intelligence and Machine Learning",meta:"3+1 years • ₹13,750 per semester • Intake 60"}
];
const SHORT_TERM_CARDS=[
 {title:"CNC Training",meta:"Short-term skill training"},
 {title:"CMM Training",meta:"Short-term skill training"},
 {title:"AutoCAD",meta:"CAD design training"},
 {title:"SolidWorks",meta:"3D CAD training"},
 {title:"CATIA",meta:"CAD / product design training"},
 {title:"CAD-CAM",meta:"Computer-aided design and manufacturing"}
];
const PLACEMENT_COMPANIES=["Dassult Systems","Goodrich Aerospace","Wipro","TCS","Infosys","IBM","Siemens","Bosch","Volvo","Toyota Kirloskar","L&T","Schneider","ABB","Mahindra","TAFE","Denso"];
const ALUMNI_COMPANIES=["Spectrum Moulds","Incite Cam","Saras Mikrons","Camtech","Macro Precise","Accu Spark","3D Precisions","Shashwathi","Precision Mould Tech","Techno Services","Shankar Tools","3D Cad","Magna Tooling","Cadwin","Benaka Tooling"];
const answers={
 timings:["GTTC Belagavi college working hours are generally 9:00 AM to 5:00 PM, Monday to Friday. Saturday may have a half-day or special schedule, and Sunday is usually a holiday.","GTTC Belagavi FAQ"],
 courses:["Diploma courses are:","GTTC Belagavi FAQ"],
 aiml:["GTTC Belagavi offers a Diploma in Artificial Intelligence and Machine Learning (AI & ML). The programme is included in the long-term diploma course options.","GTTC Belagavi FAQ"],
 admission:["For admission, students should check the current admission notification for eligibility, application dates and required documents. The chatbot can also guide students to the relevant admission information.","GTTC Belagavi FAQ"],
 fees:["The available course fee information is shown below. Fees can vary by programme, admission year or official notification.","GTTC Belagavi FAQ"],
 contact:["You can contact GTTC Belagavi through the college office for admission, course and student enquiries. The chatbot can display the current contact details when they are added to the FAQ database.","GTTC Belagavi FAQ"],
 website:["The official GTTC Belagavi centre page is available online.","Official GTTC Belagavi page"],
 library:["The GTTC Belagavi library is available for students for study and reference. Library timings may follow the college working schedule.","GTTC Belagavi FAQ"],
 exam:["Exam and internal assessment schedules are announced by the concerned department. Students should follow the latest department notification for the exact date and time.","GTTC Belagavi FAQ"],
 short_term:["Short-term training options include:","GTTC Belagavi FAQ"],
 location:["GTTC Belagavi is located in the Udyambag industrial area of Belagavi, Karnataka.","GTTC Belagavi FAQ"],
 principal:["The Principal of GTTC Belagavi, Belagavi is Shri Yallappa Savadatti Sir.","GTTC Belagavi FAQ"],
 placement:["GTTC placement information includes companies/industries where students have been placed after course completion. A separate section below also shows companies started by GTTC alumni.","GTTC Official Placement & Entrepreneurs"]
};

let last="";
const chat=document.getElementById("chat"), input=document.getElementById("input"), analysis=document.getElementById("analysis"), analysisBody=document.getElementById("analysisBody");
function esc(x){return x.replace(/[&<>"']/g,m=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[m]))}
function tok(q){return q.toLowerCase().match(/[a-z0-9]+/g)||[]}
function prep(q){return tok(q).filter(x=>!STOP.has(x))}
function classify(q){let low=q.toLowerCase(),best="unknown",score=0;for(const [name,keys] of intents){let s=0;for(const k of keys)if(low.includes(k))s+=k.includes(" ")?2:1;if(s>score){score=s;best=name}}return [best,score?Math.min(.98,.55+.12*score):0]}
function sentiment(q){let w=new Set(tok(q)),p=[...w].filter(x=>POS.has(x)).length,n=[...w].filter(x=>NEG.has(x)).length;return p>n?"Positive":n>p?"Negative":"Neutral"}
function showAnalysis(q){let t=tok(q),f=prep(q),[intent,conf]=classify(q),sent=sentiment(q);analysisBody.innerHTML=`<div><b>1. Tokenization</b><p>${t.map(x=>`<span class="tag">${esc(x)}</span>`).join("")}</p></div><div><b>2. Stopword Handling</b><p>${f.map(x=>`<span class="tag">${esc(x)}</span>`).join("")||"No content words"}</p></div><div><b>3. Intent / Pattern</b><p><span class="tag">${intent}</span></p></div><div><b>4. Confidence</b><div class="meter"><div style="width:${conf*100}%"></div></div>${Math.round(conf*100)}%</div><div><b>5. Sentiment</b><p><span class="tag">${sent}</span></p></div>`}
function addUser(q){let d=document.createElement("div");d.className="msg";d.innerHTML=`<div class="avatar uav">You</div><div><div class="role">You</div><div class="text">${esc(q)}</div></div>`;chat.appendChild(d);scroll()}
function cardHTML(items, kind="course"){return `<div class="option-list">${items.map(x=>`<div class="option-card ${kind}"><div class="option-title">${esc(x.title)}</div><div class="option-meta">${esc(x.meta||"")}</div>${x.extra?`<div class="option-extra">${esc(x.extra)}</div>`:""}</div>`).join("")}</div>`}
function answerHTML(intent){
 if(intent==="courses") return `<div class="text">Diploma courses are:</div>${cardHTML(COURSE_CARDS)}`;
 if(intent==="fees") return `<div class="text">The available course fee information is:</div>${cardHTML(COURSE_CARDS.map(x=>({title:x.title,meta:"₹13,750 per semester • "+x.meta.split("•").slice(-1)[0].trim()})),"fee")}`;
 if(intent==="short_term") return `<div class="text">Short-term courses / training options are:</div>${cardHTML(SHORT_TERM_CARDS,"training")}`;
 if(intent==="timings") return `<div class="text">GTTC Belagavi working schedule:</div>${cardHTML([{title:"Monday – Friday",meta:"9:00 AM – 5:00 PM",extra:"Regular college working hours"},{title:"Saturday",meta:"Half-day / special schedule",extra:"May vary according to the college schedule"},{title:"Sunday",meta:"Usually a holiday",extra:"Check the latest college notification for special schedules"}],"schedule")}`;
 if(intent==="aiml") return `<div class="text">GTTC Belagavi offers:</div>${cardHTML([{title:"Diploma in Artificial Intelligence and Machine Learning",meta:"3+1 years • ₹13,750 per semester • Intake 60",extra:"AI & ML long-term diploma programme"}],"aiml")}`;
 if(intent==="principal") return `<div class="text">Principal information:</div>${cardHTML([{title:"Shri Yallappa Savadatti Sir",meta:"Principal • GTTC Belagavi",extra:"College head / principal information"}],"person")}`;
 if(intent==="placement") return `<div class="text">GTTC placement information includes companies/industries where students have been placed after course completion:</div>${cardHTML(PLACEMENT_COMPANIES.map(x=>({title:x,meta:"Company listed in GTTC placement information"})),"placement") }<div class="text placement-subtitle">GTTC alumni entrepreneurs:</div>${cardHTML(ALUMNI_COMPANIES.map(x=>({title:x,meta:"Company started by GTTC alumni"})),"entrepreneur")}`;
 return `<div class="text">${esc(answers[intent]?.[0]||"Sorry, I couldn't find an answer for that question. Try asking about college timings, departments, courses, AIML, admission, fees, exams, library, short-term courses, contact, location, website, principal or placements.")}</div>`;
}
function addBot(q){let [intent,conf]=classify(q),sent=sentiment(q);let a=answers[intent]||["Sorry, I couldn't find an answer for that question. Try asking about college timings, departments, courses, AIML, admission, fees, exams, library, short-term courses, contact, location, website, principal or placements.","FAQ fallback"];let d=document.createElement("div");d.className="msg";let links=intent==="website"?`<br><a href="${OFFICIAL}" target="_blank">Open official GTTC website ↗</a>`:intent==="placement"?`<br><a href="${PLACEMENT}" target="_blank">Open official GTTC placement page ↗</a>`:"";d.innerHTML=`<div class="avatar bav">AI</div><div class="content"><div class="role">GTTC AI • ${intent}</div>${answerHTML(intent)}<div class="source">📌 ${esc(a[1])} • Sentiment: ${sent} • Confidence: ${Math.round(conf*100)}%${links}</div></div>`;chat.appendChild(d);last=a[0];showAnalysis(q);scroll()}
function scroll(){chat.scrollTop=chat.scrollHeight}
async function send(q){q=(q||input.value).trim();if(!q)return;if(document.querySelector(".welcome"))document.querySelector(".welcome").remove();addUser(q);input.value="";input.style.height="auto";let d=document.createElement("div");d.className="msg";d.id="typing";d.innerHTML=`<div class="avatar bav">AI</div><div><div class="role">GTTC AI</div><div class="typing"><i></i><i></i><i></i></div></div>`;chat.appendChild(d);scroll();await new Promise(r=>setTimeout(r,350));d.remove();addBot(q)}
document.querySelectorAll("[data-q]").forEach(b=>b.onclick=()=>send(b.dataset.q));
input.addEventListener("input",()=>{input.style.height="auto";input.style.height=Math.min(input.scrollHeight,140)+"px"});
input.addEventListener("keydown",e=>{if(e.key==="Enter"&&!e.shiftKey){e.preventDefault();send()}});
document.getElementById("send").onclick=()=>send();
document.getElementById("nlpBtn").onclick=()=>analysis.classList.toggle("show");
document.getElementById("closeAnalysis").onclick=()=>analysis.classList.remove("show");
document.getElementById("clearBtn").onclick=()=>location.reload();
document.getElementById("newChat").onclick=()=>location.reload();
function theme(){document.body.classList.toggle("dark");localStorage.gttcTheme=document.body.classList.contains("dark")?"dark":"light"}
document.getElementById("themeBtn").onclick=theme;document.getElementById("theme2").onclick=theme;
if(localStorage.gttcTheme==="dark")document.body.classList.add("dark");
document.getElementById("copyBtn").onclick=()=>{if(last)navigator.clipboard?.writeText(last)}
