# 运动后效范式：视觉运动适应的心理物理逻辑、神经机制与测量边界

视觉系统需要在持续变化的输入中维持对运动方向和速度的敏感性，同时避免近期刺激统计长期占据有限的编码范围。运动后效（motion aftereffect, MAE）为检验这一适应过程提供了经典的心理物理范式：观察者持续观看单一方向的运动后，物理静止或方向模糊的测试图案会被知觉为朝相反方向运动。由于测试阶段的视网膜输入可以保持不变，适应方向、测试类型与主观报告之间的系统关系能够用于推断方向选择性通道的状态变化。然而，MAE 并不是某个单一神经部位“疲劳”的直接读数；适应时长、空间频率、速度、注意、测试图案和报告准则都会改变测量结果（Anstis et al., 1998; Mather et al., 2008）。

MAE 研究的核心方法学价值在于把运动暴露、适应后的测试输入和知觉判断分离。静止测试所产生的静态运动后效（static motion aftereffect, sMAE）与动态噪声或反相闪烁测试所产生的动态运动后效（dynamic motion aftereffect, dMAE）具有不同的恢复和存储特性，因而不能视为同一潜变量的可互换指标（Verstraten et al., 1996）。本文围绕平移型 sMAE 的任务逻辑，综合其历史来源、行为与神经科学证据、主要应用及测量边界，并说明 TaskBeacon 当前实现与经典四孔径 Gabor 方案的对应关系。

## 1. 范式提出与理论背景

Wohlgemuth（1911）对可见运动后效进行了早期系统实验，考察了适应时长、测试条件与后效存储等问题，奠定了以“运动暴露—静止测试—消失报告”测量 MAE 持续时间的基本程序。方向相反的后效通常由方向选择性神经群体适应后的相对响应失衡解释：适应方向对应群体的响应下降，使测试输入在对手编码中的平衡偏向相反方向。后续研究表明，适应可发生于多个运动加工阶段，效应也受到刺激位置、单眼/双眼转移、局部特征与全局运动组织的共同限制，因此“单一通道被动疲劳”不足以概括全部现象（Anstis et al., 1998; Mather et al., 2008）。

Harris、Morgan 与 Still（1981）从生态信息出发提出另一项重要限制：大范围视网膜运动在自然环境中经常由观察者自身运动产生，前庭与本体感觉会参与区分自运动和环境运动；传统实验室中身体静止而视野运动的条件可能诱发视觉—前庭关系的再校准。该解释扩展了 MAE 的理论问题，但其移动观察者程序不同于固定头位、局部光栅适应的 sMAE，不能由局部平移任务直接检验。

Bex、Metha 与 Makous（1999）将四个高斯窗光栅对称置于注视点周围，通过改变各孔径内局部运动的排列，构成平移、旋转和辐射等全局运动。他们以主观持续时间、抵消后效所需的运动对比度以及突变检测阈限三种方法估计 MAE，三类指标均显示旋转和辐射条件的后效强于平移条件，并在未直接适应的位置观察到差异。该结果说明局部方向适应之外还存在对全局运动组织敏感的整合过程，也使四孔径平移条件成为控制局部能量、比较全局结构的基准。TaskBeacon 当前任务采用的正是该研究实验 1 的平移条件与静止测试持续时间法，而非其旋转或辐射条件。

## 2. 任务逻辑、流程与核心指标

经典平移型 sMAE 试次包含三个必要环节。适应阶段在固定视网膜位置呈现连续单向运动，建立方向选择性响应的不平衡；静止测试阶段在相同位置呈现具有清晰空间结构但物理不动的图案，使相反方向的主观运动得以显现；报告阶段记录后效是否出现及何时消失。适应方向与测试期知觉方向应相反，左向与右向适应的平衡安排可削弱固定按键偏好和方向基线偏移。恢复间隔用于降低跨试次残留，但其充分性取决于适应强度、测试刺激及是否发生“存储”，不能仅凭固定休息时长推定基线完全恢复（Culham et al., 1999; Verstraten et al., 1996）。

持续时间是 sMAE 最直观的因变量，即从静止测试开始到观察者判断主观运动完全消失的时间。它同时包含知觉衰减、终止准则、按键动作和注意波动，方差通常高于强迫选择抵消阈限。抵消法通过向测试图案加入与后效相反的真实运动，估计主观静止点；阈限法比较适应前后运动检测或方向辨别阈限。三者分别强调现象持续、知觉偏置和敏感性变化，不能在没有经验校准时相互换算。增益控制模型能够在限定刺激条件下联系 dMAE 持续时间、抵消阈限和方向辨别阈限，但也明确表明持续时间是高变异且依赖主观准则的测量（van de Grind et al., 2003）。

任务阶段与心理构念应保持操作对应。适应期反映近期运动统计对方向、速度和空间位置选择性响应的调节；“适应方向相反的主观运动”支持方向对手编码失衡，但不单独定位神经层级。静止测试期的后效持续时间反映适应状态、测试驱动和报告准则的共同作用。左向与右向条件的平均值可作为平移 sMAE 的总体估计，方向差异则需排除眼动、显示不对称和按键映射偏差。未报告主观运动与超过测试上限未作答在心理含义上不同：前者表示测试开始时没有可报告后效，后者是右删失观测，也可能包含漏答。

## 3. 主要行为与神经科学发现

### 3.1 方向、速度与全局运动组织

MAE 的方向反转支持方向选择性适应，但后效大小并非仅由单一适应方向决定。Bex 等（1999）在保持局部孔径刺激相近时发现复杂全局运动产生更强后效，说明全局组织改变了适应结果。近期速度研究进一步显示，视觉系统可能同时保留适应刺激在孔径约束下容许的多个速度表征，而不只适应观察者最终知觉到的单一速度；适应后的方向—速度偏移可由联合编码模型解释（Gekas & Mamassian, 2021）。因此，持续时间只能说明某种测试条件下后效存在多久，不能完整表征知觉速度或方向分布。

适应也可作用于更高阶的运动结构。Nakayama 等（2024）发现，多个物体共享的知觉轨迹倾斜能够产生排斥性的轨迹后效；效应取决于知觉轨迹而非物理朝向，并可跨视野半球转移。这类结果支持位置与运动信号整合后的可适应表征，但其轨迹判断、刺激集合和跨位置转移均不同于局部 Gabor 的平移 sMAE。它说明 MAE 家族包含多层次操作，不意味着所有后效都由同一机制生成。

### 3.2 注意、决策与跨模态应用

注意是平移型 MAE 的实质性调节变量。Bartlett 等（2019）对 29 项研究、37 个独立样本的元分析显示，注意运动特征总体上增强后续 MAE，且平移运动中的注意效应大于旋转或扩张运动；刺激大小、偏心度和速度解释了部分研究间异质性。持续注视并不保证持续注意，注意分配差异因而可能被误读为适应能力差异。

后效报告还可能包含知觉后决策成分。Gallagher、Suddendorf 与 Arnold（2021）发现，静态图像所暗示的运动改变方向分类，却未相应改变信心分布；真实运动的序列效应则同时改变判断和信心。该结果不否定真实运动适应，但表明单一分类或终止报告不足以排除准则偏移。将信心、抵消阈限或无适应基线与持续时间结合，有助于区分感觉变化与反应策略。

跨模态 MAE 将范式用于研究感觉间运动表征。综述证据显示，视觉、听觉和触觉后效的稳健性与空间参考系并不相同，跨模态转移也不能仅凭共同的行为偏移断言共享神经元（Brannick & Vibell, 2023）。在早期失聪成人中，触觉到视觉的转移得以保留，而视觉到触觉的转移减弱，提示感觉经验能够改变跨模态运动适应的不对称性（Xiao et al., 2021）。这类群体结果属于机制性比较，尚不足以把 MAE 作为个体临床诊断工具。

### 3.3 fMRI 与 EEG 证据

功能磁共振成像（functional magnetic resonance imaging, fMRI）研究首先显示，人类中颞运动复合区 hMT+/V5 在观察者观看物理静止但出现 MAE 的测试图案时活动升高，并且其时间过程与行为后效衰减相近（Tootell et al., 1995）。存储范式进一步发现，暗间隔中 hMT+ 活动较弱，合适测试图案出现、后效恢复时活动再次增强，表明 MAE 的表达依赖适应状态与测试输入的交互，而不是一个在无输入期间持续线性衰减的显性运动信号（Culham et al., 1999）。

早期 fMRI 结果仍需控制注意。Huk、Ress 与 Heeger（2001）在 MAE 与对照条件中匹配运动注意后，hMT+ 的总体活动差异消失，但方向选择性适应造成的响应不平衡仍见于 hMT+ 和更早视觉区，并与速度辨别不对称相联系。现有 fMRI 证据由此支持分布式方向选择性适应及 hMT+ 的重要参与，不支持把某一区域的 BOLD 增强直接解释为主观运动的充分原因。

脑电图（electroencephalography, EEG）补充了时间进程信息。Akyüz 等（2020）在 dMAE 中比较 640 ms 与 6.4 s 适应，二者均引起行为后效，并在测试刺激出现后 64–112 ms 的枕部及顶枕部事件相关电位上产生不同调节，较长适应的后效更强。该证据提示短时和较长时程适应很早便影响测试加工，但研究使用方向模糊的动态测试，其 ERP 结果不能直接外推到 30 s 适应后的静止持续时间报告；头皮信号也不足以精确定位发生适应的皮层来源。

## 4. 范式发展与主要应用

MAE 的方法学发展主要体现在测试刺激、测量方式和运动层级的分化。静止测试适于诱发经典方向相反的 sMAE；动态噪声或反相闪烁测试能够揭示在静止测试中不易表达的高速度或二阶运动适应。两类后效具有不同的恢复、存储和速度依赖，研究设计应依据问题选择测试，不能只以效应强弱决定版本（Mather et al., 2008; Verstraten et al., 1996）。四孔径、透明运动和复杂光流操作进一步将问题从局部方向通道扩展到全局整合、运动分割与自运动信息。

测量方式也从单次持续时间扩展到抵消阈限、心理测量函数、变化检测和计算模型。Petrov 与 Van Horn（2012）发现，方向辨别训练显著提高任务特异的辨别力，却未改变 sMAE 或 dMAE 持续时间，提示知觉学习可发生于读出权重而非早期运动表征本身。Zeljic、Solomon 与 Morgan（2024）采用较少受方向报告偏差影响的变化检测方法，在大样本筛查中观察到方向选择性适应的真实个体差异，且不能由练习或较差注视完全解释。上述工作共同要求研究者区分稳定的群体平均后效、个体排序信度与机制定位；任何一种行为指标都不应单独承担三种推论。

## 5. 测量效度与解释边界

sMAE 具有明确的表面效度和操控效度：适应运动、静止测试以及方向相反的主观运动构成可重复的条件关系。其构念效度则取决于对替代解释的控制。适应与测试的空间频率、对比度、偏心度、速度及视网膜位置会改变效应；眼动可把刺激移出已适应区域；注意不足会削弱适应；反复试次可能产生累积适应或学习；终止按键把知觉消退与反应准则、动作时间混合。固定像素而未标定视距、像素密度和亮度时，跨设备数据尤其不能按视角、空间频率或物理对比度直接合并。

持续时间法的优势是程序简单并接近主观现象，局限是高方差、上限删失和准则依赖（van de Grind et al., 2003）。效应持续到截止时应按删失数据处理，不能直接赋值为上限；从测试开始即无运动与漏答必须分开编码。方向平衡、无适应基线、重复测量和抵消阈限可提高解释力，但并不自动保证重测信度。现有文献尚未为 TaskBeacon 的八试次固定像素版本建立个体水平重测信度、常模或临床界值；近年的个体差异证据也提示，群体中存在弱适应者并不等同于异常或疾病（Zeljic et al., 2024）。因此，该范式适合检验条件操控与群体差异，不宜据单次持续时间对个体视觉功能作诊断。

## 6. TaskBeacon 中的任务实现

### 6.1 任务资源与访问入口

| 资源 | ID | 用途 | 地址 |
|---|---|---|---|
| 完整实验源码 | T000135 | PsychoPy/PsyFlow 行为实验实现 | [GitHub](https://github.com/TaskBeacon/T000135-motion-aftereffect-task) |
| 浏览器配套源码 | H000135 | 基于共享 psyflow-web 的行为型网页实现 | [GitHub](https://github.com/TaskBeacon/H000135-motion-aftereffect-task) |
| 在线运行入口 | H000135 | 直接体验八试次行为任务 | [TaskBeacon Web Runner](https://taskbeacon.github.io/psyflow-web/?task=H000135) |

T 与 H 版本均使用中文指导语，属于视觉刺激加键盘自我报告的行为任务。网页实现用于复现相同任务流程，不等同于经过显示器标定的心理物理采集，也不替代 EEG、fMRI 或临床采集系统。

### 6.2 实现流程与关键参数

![TaskBeacon 运动后效任务流程](../task_flow.png)

**图 1. TaskBeacon T000135 的试次流程。** 每次试次先呈现中央注视十字 1 s；随后四个 256 × 256 像素的高斯窗垂直 Gabor 斑在注视点上、下、左、右各偏移 128 像素处同步平移 30 s。`left` 条件的水平相位以 −4 周/秒变化，`right` 条件以 +4 周/秒变化；四个光栅在单次试次开始时相位归零。适应结束后保持最后实际呈现相位并立即进入最长 30 s 的静止测试，不绘制额外运动。观察者若曾出现运动感，在其完全消失时按空格；若测试开始即无运动感，按 N。空格反应的测试期反应时作为后效持续时间，N 记为零并保留实际按键时间；超时记为缺失且右删失。测试后仅呈现注视十字恢复 60 s。条件由每区组两个左向、两个右向试次组成，无基于反应的自适应调整。

TaskBeacon 当前版本共 2 个区组、每区组 4 次，总计 8 次，方向顺序在区组内平衡并随机化。光栅空间频率为 1/32 周/像素，标称对比度为 0.4，高斯窗标准差为 25.6 像素；显示窗口为 1280 × 800 像素、灰色背景。主要记录结果是报告类别、静止测试反应时及有效持续时间；任务不提供正确/错误或能力反馈，也不根据表现调整后续刺激。该实现保留了 Bex 等（1999）的四孔径布局、30 s 适应、4 周/秒时间频率和静止持续时间法，但将原研究的视角参数换算为固定像素比例；未强制视距、像素密度、伽马或眼动标定，因而不能声称刺激为原研究的 2 周/度、2° 偏心度或 0.4° 高斯标准差。60 s 恢复期、30 s 测试上限、N 键“从未出现”类别和两区组结构属于当前实现，现有证据不能确认 60 s 对每名观察者均足以完全消除残留适应。

## 参考文献

Akyüz, S., Pavan, A., Kaya, U., & Kafalıgönül, H. (2020). Short- and long-term forms of neural adaptation: An ERP investigation of dynamic motion aftereffects. *Cortex, 125*, 122–134. https://doi.org/10.1016/j.cortex.2019.12.015

Anstis, S., Verstraten, F. A. J., & Mather, G. (1998). The motion aftereffect. *Trends in Cognitive Sciences, 2*(3), 111–117. https://doi.org/10.1016/S1364-6613(98)01142-5

Bartlett, L. K., Graf, E. W., Hedger, N., & Adams, W. J. (2019). Motion adaptation and attention: A critical review and meta-analysis. *Neuroscience & Biobehavioral Reviews, 96*, 290–301. https://doi.org/10.1016/j.neubiorev.2018.10.010

Bex, P. J., Metha, A. B., & Makous, W. (1999). Enhanced motion aftereffect for complex motions. *Vision Research, 39*(13), 2229–2238. https://doi.org/10.1016/S0042-6989(98)00329-0

Brannick, S., & Vibell, J. F. (2023). Motion aftereffects in vision, audition, and touch, and their crossmodal interactions. *Neuropsychologia, 190*, 108696. https://doi.org/10.1016/j.neuropsychologia.2023.108696

Culham, J. C., Dukelow, S. P., Vilis, T., Hassard, F. A., Gati, J. S., Menon, R. S., & Goodale, M. A. (1999). Recovery of fMRI activation in motion area MT following storage of the motion aftereffect. *Journal of Neurophysiology, 81*(1), 388–393. https://doi.org/10.1152/jn.1999.81.1.388

Gallagher, R. M., Suddendorf, T., & Arnold, D. H. (2021). The implied motion aftereffect changes decisions, but not confidence. *Attention, Perception, & Psychophysics, 83*(8), 3047–3055. https://doi.org/10.3758/s13414-021-02331-z

Gekas, N., & Mamassian, P. (2021). Adaptation to one perceived motion direction can generate multiple velocity aftereffects. *Journal of Vision, 21*(5), Article 17. https://doi.org/10.1167/jov.21.5.17

Harris, L. R., Morgan, M. J., & Still, A. W. (1981). Moving and the motion after-effect. *Nature, 293*(5828), 139–141. https://doi.org/10.1038/293139a0

Huk, A. C., Ress, D., & Heeger, D. J. (2001). Neuronal basis of the motion aftereffect reconsidered. *Neuron, 32*(1), 161–172. https://doi.org/10.1016/S0896-6273(01)00452-4

Mather, G., Pavan, A., Campana, G., & Casco, C. (2008). The motion aftereffect reloaded. *Trends in Cognitive Sciences, 12*(12), 481–487. https://doi.org/10.1016/j.tics.2008.09.002

Nakayama, R., Tanaka, M., Kishi, Y., & Murakami, I. (2024). Aftereffect of perceived motion trajectories. *iScience, 27*(4), 109626. https://doi.org/10.1016/j.isci.2024.109626

Petrov, A. A., & Van Horn, N. M. (2012). Motion aftereffect duration is not changed by perceptual learning: Evidence against the representation modification hypothesis. *Vision Research, 61*, 4–14. https://doi.org/10.1016/j.visres.2011.08.005

Tootell, R. B. H., Reppas, J. B., Dale, A. M., Look, R. B., Sereno, M. I., Malach, R., Brady, T. J., & Rosen, B. R. (1995). Visual motion aftereffect in human cortical area MT revealed by functional magnetic resonance imaging. *Nature, 375*(6527), 139–141. https://doi.org/10.1038/375139a0

van de Grind, W. A., Lankheet, M. J. M., & Tao, R. (2003). A gain-control model relating nulling results to the duration of dynamic motion aftereffects. *Vision Research, 43*(2), 117–133. https://doi.org/10.1016/S0042-6989(02)00495-9

Verstraten, F. A. J., Fredericksen, R. E., Van Wezel, R. J. A., Lankheet, M. J. M., & Van de Grind, W. A. (1996). Recovery from adaptation for dynamic and static motion aftereffects: Evidence for two mechanisms. *Vision Research, 36*(3), 421–424. https://doi.org/10.1016/0042-6989(95)00111-5

Wohlgemuth, A. (1911). *On the after-effect of seen movement* (British Journal of Psychology Monograph Supplement No. 1). Cambridge University Press.

Xiao, K., Gao, Y., Imran, S. A., Chowdhury, S., Commuri, S., & Jiang, F. (2021). Cross-modal motion aftereffects transfer between vision and touch in early deaf adults. *Scientific Reports, 11*, 4395. https://doi.org/10.1038/s41598-021-83960-0

Zeljic, K., Solomon, J. A., & Morgan, M. J. (2024). Individual differences in direction-selective motion adaptation revealed by change-detection performance. *Vision Research, 225*, 108490. https://doi.org/10.1016/j.visres.2024.108490
