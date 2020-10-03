
# Speakers' Corner

Named after the renowned corner of Hyde Park in London, the Speakers' Corner seminars are a platform
for everyone who would like to share their research. Do you have a new preprint and want to create an accompanying video lecture or just a cool result you would like to share with the community? Speakers' corner allows you to create, advertise and share your talk via Virtual Science Forum platform.

### Give a talk
The series is hence on a "self-invitation" basis, where you register for giving a talk through the [Registration Form](https://github.com/virtualscienceforum/virtualscienceforum/issues/new?template=speakers_corner_application.md) and
bring your own audience. Every week, an announcement email is sent to the Speakers' Corner mailing list (register [here](mailinglist.md)) 
containing all of the upcoming talks. That way, more potential participants will learn about your talk and may decide to join.

### How it works

1. Pick the topic of your talk, date and time (must be at least two weeks in the future), and make sure all your co-authors know about your presentation and agree.
2. Fill in the [Registration Form](https://github.com/virtualscienceforum/virtualscienceforum/issues/new?template=speakers_corner_application.md)
3. VSF:
  - checks availability of your time slot and confirm the date
  - creates the zoom meeting, opens the registration, and gives you the host key
  - announces your talk in the VSF Speakers' Corner mailing list and on this website
4. Make sure to advertise your talk and invite participants to register for the talk
5. You are welcome to moderate your talk yourself as well as invite a colleague to be your moderator
6. VSF records your talk, forwards it to you afterwards and then publishes it in out dedicated [YouTube channel](https://www.youtube.com/channel/UCvQEx4iW7u_x3jX742kUZLw)


## Schedule

Al times are shown in <span id="timezone">UTC</span> timezone.

|   Date   |     Speaker    | Title |
|:---------:|:--------------:|:-----:|
| <time datetime="2020-11-17T15:00:00+00:00">November 17 Nov:00 UTC</time> | Joshuah T. Heath | [Landau Quasiparticles in Weak Power-Law Liquids](#landau-quasiparticles-in-weak-power-law-liquids) |
| <time datetime="2020-11-20T15:00:00+00:00">November 20 Nov:00 UTC</time> | André Melo | [Conductance asymmetries in mesoscopic superconducting devices due to finite bias](#conductance-asymmetries-in-mesoscopic-superconducting-devices-due-to-finite-bias) |

## Upcoming talks


### Landau Quasiparticles in Weak Power-Law Liquids
#### Joshuah T. Heath (Boston College)

> The failure of Landau-Fermi liquid theory is often considered a telltale sign of universal, scale-invariant behavior in the emergent field theory of interacting fermions. Nevertheless, there exist borderline cases where weak scale invariance coupled with particle-hole asymmetry can coexist with the Landau quasiparticle paradigm. In this letter, I show explicitly that a Landau-Fermi liquid can exist for weak power-law scaling of the retarded Green's function. Such an exotic variant of the traditional Fermi liquid, although exhibiting a finite quasiparticle weight and large quasiparticle lifetime, is shown to always be incompatible with Luttinger's theorem for any non-trivial scaling. This result yields evidence for a Fermi liquid-like ground state in the high-field, underdoped pseudogap phase of the high-temperature cuprate superconductors.
>
> **Authors:** Joshuah T. Heath  
> **Preprint:** [arXiv:2001.08230](https://arxiv.org/abs/2001.08230)



### Conductance asymmetries in mesoscopic superconducting devices due to finite bias
#### André Melo (Kavli Institute of Nanoscience, Delft University of Technology)

> Tunneling conductance spectroscopy in normal metal-superconductor junctions is an important tool for probing Andreev bound states in mesoscopic superconducting devices, such as Majorana nanowires. In an ideal superconducting device, the subgap conductance obeys specific symmetry relations, due to particle-hole symmetry and unitarity of the scattering matrix. However, experimental data often exhibits deviations from these symmetries or even their explicit breakdown. In this work, we identify a mechanism that leads to conductance asymmetries without quasiparticle poisoning. In particular, we investigate the effects of finite bias and include the voltage dependence in the tunnel barrier transparency, finding significant conductance asymmetries for realistic device parameters. It is important to identify the physical origin of conductance asymmetries: in contrast to other possible mechanisms such as quasiparticle poisoning, finite-bias effects are not detrimental to the performance of a topological qubit. To that end we identify features that can be used to experimentally determine whether finite-bias effects are the source of conductance asymmetries.
>
> **Authors:** André Melo, Chun-Xiao Liu, Piotr Rożek, Tómas Örn Rosdahl, Michael Wimmer  
> **Preprint:** [arXiv:2008.01734](https://arxiv.org/abs/2008.01734)




## Recordings




<script>
document.getElementById("timezone").innerText = Intl.DateTimeFormat().resolvedOptions().timeZone
for (let time of document.getElementsByTagName("time")) {
    time.innerText = dayjs(time.dateTime).local().format("MMMM d h:mm");
};
</script>
